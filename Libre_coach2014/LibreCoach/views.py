from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response

from SiteWeb import settings
from librecoach import models
from librecoach.models import Stock, Annonce, User
from librecoach.serializers import StockSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import CreateAccountform,Loginform, Contactform
from django import forms
from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import auth

class IndexView(generic.ListView):
	form_class = Loginform
	template_name = 'librecoach/index.html'

	# affichage formulaire vierge
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		all_annonces = Annonce.objects.all()

		form = Loginform(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
		login(request, user)
		print(request.user.is_authenticated())

		# redirect
		return render(request, self.template_name, {"form": form, "all_annonces": all_annonces})

	def get_queryset(self):
		return Annonce.objects.filter(pris_en_charge='False')

	def logout(request):
		auth.logout(request)
		return redirect('librecoach:index')

class DetailView(generic.DetailView):
		model = Annonce
		template_name = 'librecoach/detail_annonce.html'

class ClientView(generic.ListView):
		model = User
		template_name = 'librecoach/detail_client.html'
		def get_queryset(self):
			return Annonce.objects.filter(prenom='Brady')


class PageView(generic.ListView):
		model = Annonce
		template_name = 'librecoach/page.html'

class CompteView(generic.DetailView):
		model = User
		template_name = 'librecoach/compte_client.html'


class AnnonceCreate(CreateView):
	model = Annonce
	fields = ['nom','prenom','email','telephone','pays','ville','code_postal','rubrique','titre_annonce','descriptif_annonce','user']

class AnnonceUpdate(UpdateView):
	model = Annonce
	fields = '__all__'

class AnnonceDelete(DeleteView):
	model = Annonce
	success_url = reverse_lazy('librecoach:index')

class StockList(APIView):
	def get(self, request):
		stocks = Stock.objects.all()
		serializer = StockSerializer(stocks, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class LoginView(generic.DetailView):
	form_class = Loginform
	template_name = 'librecoach/connexion/login.html'
	template_name2 = 'librecoach/index.html'

	# affichage formulaire vierge
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		all_annonces = Annonce.objects.all()

		form = Loginform(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
		login(request,user)
		print(request.user.is_authenticated())

		#redirect
		return render(request, self.template_name, {"form": form, "all_annonces":all_annonces})

class UserFormView(View):
	form_class = CreateAccountform
	template_name = 'librecoach/registration_form.html'

	#affichage formulaire vierge
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form':form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			#cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			user.set_password(password)
			user.save()

			#return si tout est okay
			user = authenticate(username=username,password=password,first_name=first_name,last_name=last_name)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('librecoach:index')

		return render(request, self.template_name, {'form': form})
