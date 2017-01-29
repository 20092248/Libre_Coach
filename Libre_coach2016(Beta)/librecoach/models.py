from datetime import datetime
from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.core.urlresolvers import reverse

type_rubrique = (
    ('FAMILLE', 'Famille'),
    ('MAISON', 'Maison'),
    ('SANTE', 'Sante'),
	('TRAVAIL', 'Travail'),
	('LOISIRS', 'Loisirs'),
)

journee = (
	('INDISPONIBLE','indisponible'),
    ('MATIN', 'matin'),
    ('APRES-MIDI', 'apres-midi'),
    ('LA JOURNEE', 'la journee'),
)

class Coach(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default='inconnu')
	specialiste = models.CharField(max_length=30, choices=type_rubrique)
	coach_image = models.FileField()

	def __str__(self):
		return self.specialiste

class Annonce(models.Model):

	username = models.CharField(max_length=30, default='--')
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	telephone = models.CharField(max_length=30)
	pays = models.CharField(max_length=30)
	ville = models.CharField(max_length=30)
	code_postal = models.CharField(max_length=30)

	#user qui se cache dans rubrique
	rubrique = models.ForeignKey(Coach, blank=True, null=True)

	titre_annonce = models.CharField(max_length=100)
	descriptif_annonce = models.TextField()
	date_depot = models.DateTimeField(default=datetime.now())
	pris_en_charge = models.BooleanField(default=False)

	lundi = models.CharField(max_length=30, choices=journee, default='00')
	mardi = models.CharField(max_length=30, choices=journee, default='00')
	mercredi = models.CharField(max_length=30, choices=journee, default='00')
	jeudi = models.CharField(max_length=30, choices=journee, default='00')
	vendredi = models.CharField(max_length=30, choices=journee, default='00')
	user = models.ForeignKey(User, blank=True, null=True)


	def get_absolute_url(self):
		return reverse('librecoach:detail-annonce',kwargs={'pk': self.pk})

	def __str__(self):
		return self.titre_annonce

#Exemple pour m'entrainer
class Stock(models.Model):
	ticket = models.CharField(max_length=20)
	open = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
