from cmath import log
import imp
from optparse import OptParseError
from django.conf import settings
from django.contrib.auth import login as django_login
from django.db import OperationalError
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
import re
import os
import logging
import subprocess

logger = logging.getLogger("HMS-Login-Logger")
logger.setLevel(logging.INFO)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

class Http403Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if HttpResponseForbidden.status_code == response.status_code:
            logger.info("User login session token timed out")
            return login(request, "<span style='color:red;'>Your session has timed out, please log back in to refresh your session.</span>")
        else:
            return response


def login(request):
    next_page = request.GET.get('next')
    message = ""
    delete_message = False
    if "message" in request.COOKIES.keys():
        message = request.COOKIES["message"]
        delete_message = True
    html = render_to_string('login_page.html', {
        'TITLE': 'HMS Login', 'next': next_page, 'TEXT': message
    }, request=request)
    response = HttpResponse()
    response.write(html)
    if delete_message:
        response.delete_cookie('message')
    return response

class RequireLoginMiddleware:
    def __init__(self, get_response):

        self.login_verbose = settings.LOGIN_VERBOSE
        self.login_duration = settings.LOGIN_DURATION

        if not settings.LOGIN_REQUIRED:
            return

        self.get_response = get_response
        self.login_url = re.compile(settings.LOGIN_URL)
        self.hms_username = "hmsuser"
        self.open_urls = [
            '/hms/login'
        ]

        hms_password = self.load_password()
        if hms_password is None:
            logger.warn("HMS login password as not set.")
            return

        try:
            if not User.objects.filter(username=self.hms_username).exists():
                _user = User.objects.create_user(self.hms_username, 'hms@hms.hms', hms_password)
                _user.save()
        except Exception:
            logger.warn(f"User: {self.hms_username} already exists")

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def load_password(self):
        hms_password = os.getenv('HMS_PASS')
        if hms_password is None:
            if self.login_verbose:
                logger.info(f"Unable to get password as HMS_PASSWORD env was not set.")
            return None

        reset_env = ""
        if os.name == 'posix':
            reset_env = 'export HMS_PASS=hmspass'
        elif os.name == 'nt':
            reset_env = 'setx HMS_PASS hmspass'
        subprocess.Popen(reset_env, shell=True).wait()
        #hms_password = "hmspass"
        return hms_password

    def login_auth(self, request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        next_page = request.POST.get('next')

        print(f"Username: {username} , Password: {password}, Next Page: {next_page}")
        logger.info(f"Username: {username} , Password: {password}, Next Page: {next_page}")

        # Redirect back to login page if username is invalid
        if username != self.hms_username:
            if self.login_verbose:
                logger.info(f"Login Auth: Username is invalid. Provided username: {username}")
                print(f"Login Auth: Username is invalid. Provided username: {username}")
            response = redirect('/hms/login?next={}'.format(next_page))
            response.set_cookie('message', "Username is not correct.")
            return response
       # try:
       
#        usertest = username == 'hmsuser'
 #       passtest = password == 'hmspass'
  #      print(f"USER TEST: {usertest} , PASS TEST: {passtest}")
   #     if (username == 'hmsuser') and (password == 'hmspass'):
    #        logger.info(f"User login successful, redirecting to {next_page}.")
     #       print(f"User login successful, redirecting to {next_page}.")
      #      response = redirect('{}'.format(next_page))
       #     response.set_cookie('message', "Did not redirect")
        #    return response
        
        user = authenticate(username=username, password=password)
        session_duration = self.login_duration
        if user is not None:
            if user.is_active:
                if self.login_verbose:
                    logger.info(f"User login successful, redirecting to {next_page}, session will expire in {session_duration} secs.")
                request.session.set_expiry(session_duration)
                django_login(request, user)
                return redirect(next_page)
            else:
                if self.login_verbose:
                    logger.info(f"User no longer active, must log back in.")
                response = redirect('/hms/login?next={}'.format(next_page))
                response.set_cookie('message', "Session has ended, must log back in.")
                return response
        else:
            if self.login_verbose:
                logger.info(f"User not logged in.")
            response = redirect('/hms/login?next={}'.format(next_page))
            response.set_cookie('message', "Password is not correct.")
            return response
     #   except OperationalError:
      #      session_duration = self.login_duration
       #     if self.login_verbose:
        #        logger.info(f"User login successful, redirecting to {next_page}, session will expire in {session_duration} secs.")
         #   return redirect(next_page)
        

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path
        redirect_path = request.POST.get('next', "")
        token = request.GET.get('token')
        user = request.user
        if self.login_verbose:
            logger.info(f"Process view; user: {user}, next: {redirect_path}, token: {token}")
        if request.POST and self.login_url.match(path):
            return self.login_auth(request)
        elif not user.is_authenticated:
            if self.open_url_check(path=path):
                if self.login_verbose:
                    logger.info(f"Process view cleared open url for path: {path}")
                return
            else:
                return redirect('/hms/login?next={}'.format(path))
        elif user.is_authenticated:
            return
        else:
            return redirect('/hms/login?next={}'.format(path))

    def open_url_check(self, path):
        if any(p in path for p in self.open_urls):
            return True
        return False
