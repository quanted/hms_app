FROM continuumio/miniconda3:4.10.3p0-alpine as base

ENV CONDA_ENV_BASE=pyenv

COPY requirements.txt /tmp/requirements.txt

RUN conda create -n $CONDA_ENV_BASE python=3.9
RUN conda config --add channels conda-forge
RUN conda run -n $CONDA_ENV_BASE --no-capture-output pip install -r /tmp/requirements.txt && \
    conda run -n $CONDA_ENV_BASE --no-capture-output conda clean -afy && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.pyc' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete
RUN conda install -n $CONDA_ENV_BASE uwsgi

FROM continuumio/miniconda3:4.10.3p0-alpine as prime

ARG APP_USER=www-data
ARG CONDA_ENV_BASE
ENV CONDA_ENV=/home/www-data/pyenv
RUN adduser -S $APP_USER -G $APP_USER

RUN apk update
RUN apk upgrade
RUN pip install -U pip

WORKDIR /src/hms_app
COPY . /src/hms_app
COPY --from=base /opt/conda/envs/pyenv $CONDA_ENV

COPY uwsgi.ini /etc/uwsgi/

RUN chown -R ${APP_USER}:${APP_USER} /src/hms_app
RUN chown ${APP_USER}:${APP_USER} $CONDA_ENV
ENV DJANGO_SETTINGS_MODULE "settings"
EXPOSE 8080

ENV PYTHONPATH="/src:/src/hms_app:${PYTHONPATH}"
ENV PATH="/src:/src/hms_app:${PATH}"
USER $APP_USER

CMD ["conda", "run", "-p", "$CONDA_ENV", "--no-capture-output", "sh", "/src/hms_app/docker-start.sh"]