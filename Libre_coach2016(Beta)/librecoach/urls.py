from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from SiteWeb import settings
from django.conf.urls.static import static
from . import views

app_name= 'librecoach'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #page modele exemple
    #url('^page/$',views.PageView.as_view(), name='page'),

    # ____________________utilisateur___________________#
    url('^login/$',views.LoginView.as_view(), name='login'),
    url('^creercompte/$', views.UserFormView.as_view(), name='creer-compte'),
    url(r'^compteclient/(?P<pk>[0-9]+)/$', views.CompteView.as_view(), name='compte-client'),
    url(r'^client/(?P<pk>[0-9]+)/$', views.ClientView.as_view(), name='detail-client'),

    #____________________annonce___________________#
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail-annonce'),
    # / librecoach/annonce/ajouter/
    url(r'annonce/ajouter/$', views.AnnonceCreate.as_view(), name='annonce-ajouter'),
    # / librecoach/annonce/2/
    url(r'annonce/(?P<pk>[0-9]+)/$', views.AnnonceUpdate.as_view(), name='annonce-modifier'),
    # / librecoach/annonce/2/supprimer
    url(r'annonce/(?P<pk>[0-9]+)/supprimer/$', views.AnnonceDelete.as_view(), name='annonce-supprimer'),

    # ____________________coach___________________#
    url('^connexion/$', views.CoachView.as_view(), name='coach-view'),
    # / librecoach/annonce/coach/2/
    url(r'annonce/coach/(?P<pk>[0-9]+)/$', views.AnnonceUpdate2.as_view(), name='annonce-coach-modifier'),
    # / librecoach/coach/annonce/2/supprimer
    url(r'coach/annonce/(?P<pk>[0-9]+)/supprimer/$', views.AnnonceDelete2.as_view(), name='annonce-supprimer2'),

    # ____________________administrateur___________________#
    url('^administrateur/$',views.IndexAdm.as_view(), name='page'),
    url('^administrateur/coach/$', views.CoachFormView.as_view(success_url='../'), name='admin-coach'),
    url('^administrateur/client/$', views.UserFormViewAdm.as_view(), name='admin-client'),


    #JSON file -----> pour ex créer une application mobile
    url(r'^JSONannonce/', views.AnnonceList.as_view()),
    url(r'^JSONuser/', views.UserList.as_view()),
    url(r'^JSONcoach/', views.CoachList.as_view()),

    #USER AUTH URL
    url(r'^accueil/$',views.IndexView.logout, name='accueil'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)