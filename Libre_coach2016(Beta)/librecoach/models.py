from datetime import datetime
from django.contrib.auth.models import User
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
    ('LA_JOURNEE', 'la_journee'),
)

class Coach(models.Model):
	nom_coach = models.CharField(max_length=30)
	prenom_coach = models.CharField(max_length=30)
	specialiste = models.CharField(max_length=30, choices=type_rubrique)
	coach_image = models.CharField(max_length=1000, default='---------')

	def __str__(self):
		return self.nom_coach +' + '+ self.prenom_coach

class Annonce(models.Model):

	username = models.CharField(max_length=30, default='-------')
	nom = models.CharField(max_length=30)
	prenom = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	telephone = models.CharField(max_length=30)
	pays = models.CharField(max_length=30)
	ville = models.CharField(max_length=30)
	code_postal = models.CharField(max_length=30)
	rubrique = models.CharField(max_length=30, choices=type_rubrique)
	titre_annonce = models.CharField(max_length=100)
	descriptif_annonce = models.TextField()
	date_depot = models.DateTimeField(default=datetime.now())
	pris_en_charge = models.BooleanField(default=False)

	lundi = models.CharField(max_length=30, choices=journee, default='---------')
	mardi = models.CharField(max_length=30, choices=journee, default='---------')
	mercredi = models.CharField(max_length=30, choices=journee, default='---------')
	jeudi = models.CharField(max_length=30, choices=journee, default='---------')
	vendredi = models.CharField(max_length=30, choices=journee, default='---------')
	user = models.ForeignKey(User, blank=True, null=True)
	coach = models.ForeignKey(Coach, blank=True, null=True)

	def get_absolute_url(self):
		return reverse('librecoach:detail-annonce',kwargs={'pk': self.pk})

	def __str__(self):
		return self.titre_annonce

class Stock(models.Model):
	ticket = models.CharField(max_length=20)
	open = models.FloatField()
	close = models.FloatField()
	volume = models.IntegerField()
