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
        context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
        group_id = UserProfile.objects.filter(user = context['user']).values()[0]['group_id']
        print group_id
        group = FundraisingGroup.objects.get(id = group_id)
        context['current'] = group.current
        context['goal'] = group.goal
        return render(request, 'GroupHomePage.html', context)

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
                        #try:
                        group = FundraisingGroup.objects.get(group_code = group_code)
                        user = User.objects.create_user(username=username, email=None, password=password)
                        userProfile = UserProfile(user = user, group = group) 
                        userProfile.save()
                        #except:
                        #        context['loginMessage'] = "Invalid Group Code."
                        #        return render(request, 'register.html', context)
		
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
        #FundraisingGroup(group_name = "team america", fundraiser_name = "PoP", group_code='a').save()
        #print FundraisingGroup.objects.all().values()
        if 'r' in request.GET and request.GET['r'] == "1":
                ext_color = 'w'
                if 'extw' in request.POST:
                        ext_color = 'w'
                elif 'extg' in request.POST:
                        ext_color = 'g'
                elif 'extr' in request.POST:
                        ext_color = 'r'
                elif 'exty' in request.POST:
                        ext_color = 'y'

                int_color = 'b'
                if 'intb' in request.POST:
                        int_color = 'b'
                elif 'intg' in request.POST:
                        int_color = 'g'
                elif 'inty' in request.POST:
                        int_color = 'y'

                outhouse_color = 'b'
                if 'outhouseb' in request.POST:
                        outhouse_color = 'b'
                elif 'outhousew' in request.POST:
                        outhouse_color = 'w'

                school = School(ext_color = ext_color, int_color = int_color, outhouse_color = outhouse_color).save()
                group_id = UserProfile.objects.filter(user = context['user']).values()[0]['group_id']
                group = FundraisingGroup.objects.get(id = group_id)
                group.school_id = school
                group.save()
                print FundraisingGroup.objects.all().values()
                print School.objects.all().values()
                return render(request, 'controlpanel.html', context)
        else:
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

def edit_about(request):
        context = {'pageType': 0, 'loginMessage': "none", 'user': request.user}
	return render(request, 'editAbout.html',context)
        
