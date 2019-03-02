from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import json
import os
import socket
import time as TM
from shutil import copyfile
import pickle

import datetime as date
import pandas as pd

def home(request):
    return render(request, 'index.html' , {})