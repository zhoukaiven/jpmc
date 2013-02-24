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
                redirect('controlpanel.html')
        if 'username' not in request.POST:
                return render(request, 'login.html', context)

        #Authenticate user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
                auth_login(request, user)
                context['user'] = user
                return render(request, 'controlpanel.html', context)
        else:
                context['loginMessage'] = "Invalid user/password combination!"
                return render(request, 'login.html', context) #should be control_panel.html
    
#Called when user logs out
def logout(request):
	auth_logout(request)
	return redirect('index.html')

#The "Home" page
def index(request):
	context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	if request.user.is_authenticated():
		return render(request, 'controlpanel.html', context) 
	else:
		#return render(request, 'indexlo.html', context)
                return render(request, 'GroupHomePage.html', context)

def group_home_page(request):
        return render(request, 'GroupHomePage.html')

#Registration page, needs to be changed
def register(request):
	context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	if 'r' in request.GET and request.GET['r'] == "1":
		username = request.POST['username']
		group_code = request.POST['group']
		password = request.POST['password']
		confpassword = request.POST['confpassword']
		if not username or not password:
			context['loginMessage'] = "Please enter both username and password"
			return render(request, 'register.html', context)
                elif not group_code:
                        context['loginMessage'] = "Please enter the group code"
                        return render(request, 'register.html', context)
		elif password != confpassword:
			context['loginMessage'] = "Please make sure confirm is same as password"
			return render(request, 'register.html', context)
		
		if User.objects.filter(username = username):
                        context['loginMessage'] = "Username taken"
			return render(request, 'register.html', context)
		else:
                        try:
                                group = FundraisingGroup.objects.filter(group_code = group_code)
                                user = User.objects.create_user(username=username, email=None, password=password)
                                userProfile = UserProfile(user = user, group = group) 
                                userProfile.save()
                        except:
                                context['loginMessage'] = "Invalid Group Code."
                                return render(request, 'register.html', context)
		
		if user is not None:
			context['loginMessage'] = "Registration Successful!"
			return render(request, 'login.html', context)
		else:
			context['loginMessage'] = "Registration Failed!"
			return render(request, 'register.html', context)		
	else:
		if request.user.is_authenticated():
			return render(request, 'controlpanel.html', context)
		else:
			return render(request, 'register.html', context)

def control_panel(request):
        context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
        if request.user.is_authenticated():
		return render(request, 'controlpanel.html', context)
	else:
		return render(request, 'login.html', context)
"""
def update_control_panel(request):
"""         
def school_designer(request):
        context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
        if request.user.is_authenticated():
		return render(request, 'schoolDesigner.html',context)
	else:
		return render(request, 'login.html', context)
"""
def school_designer_update(request)
"""
def multimedia(request):
        context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	return render(request, 'multimedia.html',context)

        
