#encoding: utf-8
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.contrib import  messages
from core.forms import CampusForm
from .models import Teacher


@login_required()
def dashboard(request):
	if request.user.is_authenticated():
		user = request.user
	return render(request, 'core/dashboard.html', {'user': user})

def login(request):
	msg = []

	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']


		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				user_login(request, user)
				return redirect('/dashboard')
			else:
				messages.add_message(request, messages.WARNING, 'Usuário desativado.')
				#msg.append('Usuário desativado.')
		else:
			messages.add_message(request, messages.ERROR, 'Usuário ou senha inválido.')


			#msg.append('Usuário ou senha invalido.')	




	return render(request, 'core/login.html', {'errors': msg})

def logout(request):
	user_logout(request)
	return redirect('/login')	

@login_required()
def add_Campus(request):
	form = CampusForm()

	if request.method == 'POST':
		form = CampusForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form' : form}

	return render(request, 'core/add_Campus.html', context)

@login_required()
def professors_list(request):
	professors = Teacher.objects.all()
	return render(request, 'core/professors/index.html', {'professors':professors})

@login_required()
def professors_add(request):
	return render(request, 'core/professors/create.html')
