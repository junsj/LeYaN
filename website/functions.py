#ufo URL Configuration

from django.shortcuts import render
from django.template import loader,Context
from django.shortcuts import render_to_response
from django.http import request
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib.auth import authenticate,login,logout

from website.models import *
