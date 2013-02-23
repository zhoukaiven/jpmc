import time
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from internals.models import *

#Called when user logs in
def login(request):
	#Context
	context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	
	#Check if already logged in
	if request.user.is_authenticated():
		redirect('index.html')
	if 'username' not in request.POST:
		return render(request, 'indexlo.html', context)
	
	#Authenticate user
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		auth_login(request, user)
		context['user'] = user
		redirect('index.html')
	else:
		context['loginMessage'] = "Invalid password!"
		return render(request, 'indexlo.html', context)
    
#Called when user logs out
def logout(request):
	auth_logout(request)
	return redirect('index.html')

#The "Home" page
def index(request):
	context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	if request.user.is_authenticated():
		return render(request, 'index.html', context)
	else:
		return render(request, 'indexlo.html', context)
