from django.core.mail import send_mail
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response

from SiteWeb import settings
from librecoach import models
from librecoach.models import Stock, Annonce, User, Coach
from librecoach.serializers import AnnonceSerializer, UserSerializer, CoachSerializer
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import CreateAccountform,Loginform, CreateAccountformAdm, ContactForm
from django import forms
from django.shortcuts import render, render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
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

class FaqView(TemplateView):
		template_name = 'librecoach/faq.html'

class ClientView(generic.ListView):
		model = User
		template_name = 'librecoach/detail_client.html'

		def get_queryset(request):
			return Annonce.objects.all()



class IndexAdm(generic.ListView):
		model = Annonce
		template_name = 'librecoach/administrateur.html'

		def get_queryset(self):
			return Coach.objects.all()

class CompteView(generic.DetailView):
		model = User
		template_name = 'librecoach/compte_client.html'


class AnnonceCreate(CreateView):
	model = Annonce
	fields = ['username','nom','prenom','email','telephone','pays','ville','code_postal','rubrique','titre_annonce','descriptif_annonce','lundi','mardi','mercredi','jeudi','vendredi','user']

class AnnonceUpdate(UpdateView):
	model = Annonce
	fields = ['nom','prenom','email','telephone','pays','ville','code_postal','rubrique','titre_annonce','descriptif_annonce','lundi','mardi','mercredi','jeudi','vendredi']

class AnnonceUpdate2(UpdateView):
	model = Annonce
	fields = ['pris_en_charge']

class AnnonceDelete(DeleteView):
	model = Annonce
	u = Annonce.objects.all()
	def get_success_url(self):
		return reverse_lazy('librecoach:index')

class AnnonceDelete2(DeleteView):
	model = Annonce
	success_url = reverse_lazy('librecoach:index')

class AnnonceList(APIView):
	def get(self, request):
		a = Annonce.objects.all()
		serializer = AnnonceSerializer(a, many=True)
		return Response(serializer.data)

	def post(self):
		pass
class UserList(APIView):
	def get(self, request):
		u = User.objects.all()
		serializer = UserSerializer(u, many=True)
		return Response(serializer.data)

	def post(self):
		pass
class CoachList(APIView):
	def get(self, request):
		c = Coach.objects.all()
		serializer = CoachSerializer(c, many=True)
		return Response(serializer.data)

	def post(self):
		pass

class CoachView(DetailView):
	form_class= Loginform
	template_name = 'librecoach/connexion/coach_login.html'
	template_name2 = 'librecoach/connexion/detail_coach.html'

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
		return render(request, self.template_name2, {"form": form, "all_annonces": all_annonces})

class LoginView(generic.DetailView):
	form_class = Loginform
	template_name = 'librecoach/connexion/login.html'

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

class UserFormViewAdm(View):
	form_class = CreateAccountformAdm
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
					return redirect('librecoach:admin-coach')

		return render(request, self.template_name, {'form': form})

class CoachFormView(CreateView):
	model = Coach
	fields = ['user','specialiste','coach_image']

class UpdateCoachFormView(UpdateView):
	model = Coach
	fields = '__all__'
	success_url = '../../../'

class DeleteCoachFormView(DeleteView):
	model = Coach
	success_url = '../../../'

class ClientListView(generic.ListView):
		model = User
		template_name = 'librecoach/user_list.html'
		def get_queryset(self):
			return User.objects.filter(is_staff='False')

class CoachListView(generic.ListView):
		model = User
		template_name = 'librecoach/coach_list.html'
		def get_queryset(self):
			return User.objects.filter(is_staff='True')

class UpdateClientFormView(UpdateView):
	model = User
	template_name = 'librecoach/user_form.html'
	fields = '__all__'
	success_url = '../liste/'

class DeleteClientFormView(DeleteView):
	model = User
	success_url = '../../../'


class ContactMailView(FormView):
	template_name = 'librecoach/contact_mail.html'
	form_class = ContactForm
	success_url = '../'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.send_mail()

		return super(ContactMailView, self).form_valid(form)