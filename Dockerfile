FROM continuumio/miniconda3:23.5.2-0-alpine AS base

ENV CONDA_ENV_BASE=pyenv

COPY requirements.txt /tmp/requirements.txt

RUN conda config --add channels conda-forge
RUN conda create -n $CONDA_ENV_BASE python=3.10
RUN conda run -n $CONDA_ENV_BASE --no-capture-output pip install -r /tmp/requirements.txt && \
    conda run -n $CONDA_ENV_BASE --no-capture-output conda clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete
RUN conda install -n $CONDA_ENV_BASE uwsgi=2.0.22

FROM continuumio/miniconda3:23.5.2-0-alpine AS prime

ARG APP_USER=www-data
ARG CONDA_ENV_BASE=/opt/conda/envs/pyenv
ENV CONDA_ENV=/home/www-data/pyenv
RUN adduser -S $APP_USER -G $APP_USER

RUN apk update
RUN apk upgrade
RUN apk upgrade busybox --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main


WORKDIR /src/hms_app
COPY . /src/hms_app
COPY --from=base $CONDA_ENV_BASE $CONDA_ENV_BASE


# (8/18/23) Added for prisma scans:
RUN conda update cryptography

# Removes all pips from image to "resolve" open Prisma CVE:
# (NOTE: No very sustainable, will break with higher version of Python.)
RUN rm -rf /home/www-data/pyenv/lib/python3.10/site-packages/pip* \
    /home/www-data/pyenv/bin/pip \
    /opt/conda/lib/python3.10/site-packages/pip* \
    /opt/conda/envs/pyenv/lib/python3.10/site-packages/pip-* \
    /opt/conda/bin/pip \
    /root/.cache/pip

# Removing some test keys that Prisma thinks are an issue (they're not):
RUN rm /opt/conda/envs/pyenv/lib/python3.10/site-packages/tornado/test/test.key || true
RUN rm /opt/conda/pkgs/conda-content-trust-0.1.1-pyhd3eb1b0_0/info/test/tests/testdata/test_key_1_268B62D0.pri.asc || true
RUN rm /opt/conda/pkgs/conda-content-trust-0.1.1-pyhd3eb1b0_0/info/test/tests/testdata/test_key_2_7DB43643.pri.asc || true


COPY uwsgi.ini /etc/uwsgi/

RUN chown -R ${APP_USER}:${APP_USER} /src/hms_app
RUN chown ${APP_USER}:${APP_USER} $CONDA_ENV_BASE
EXPOSE 8080

USER $APP_USER
ENV DJANGO_SETTINGS_MODULE="settings"

ENV PYTHONPATH="/src:/src/hms_app:$PYTHONPATH"
ENV PATH="/bin:/src:/src/hms_app:$PATH"

#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["conda", "run", "-n", "pyenv", "--no-capture-output", "sh", "/src/hms_app/docker-start.sh"]
