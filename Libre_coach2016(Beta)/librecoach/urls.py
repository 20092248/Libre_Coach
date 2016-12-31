from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from SiteWeb import settings
from django.conf.urls.static import static
from . import views

app_name= 'librecoach'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url('^page/$',views.PageView.as_view(), name='page'),

    url('^creercompte/$',views.UserFormView.as_view(), name='creer-compte'),

    url('^login/$',views.LoginView.as_view(), name='login'),

    url('^connexion/$',views.CoachView.as_view(), name='coach-view'),
    #url('^contact/$',views.ContactView.contact, name='login'),

    url(r'^client/(?P<pk>[0-9]+)/$', views.ClientView.as_view(), name='detail-client'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail-annonce'),

    url(r'^compteclient/(?P<pk>[0-9]+)/$', views.CompteView.as_view(), name='compte-client'),
    # / librecoach/annonce/ajouter/
    url(r'annonce/ajouter/$', views.AnnonceCreate.as_view(), name='annonce-ajouter'),

    # / librecoach/annonce/2/
    url(r'annonce/(?P<pk>[0-9]+)/$', views.AnnonceUpdate.as_view(), name='annonce-modifier'),

# / librecoach/annonce/coach/2/
    url(r'annonce/coach/(?P<pk>[0-9]+)/$', views.AnnonceUpdate2.as_view(), name='annonce-coach-modifier'),

    # / librecoach/annonce/2/supprimer
    url(r'annonce/(?P<pk>[0-9]+)/supprimer/$', views.AnnonceDelete.as_view(), name='annonce-supprimer'),

    #JSON file
    url(r'^stocks/', views.StockList.as_view()),

    #USER AUTH URL
    #url(r'^login/$',views.LoginView.as_view(), name='login'),
    url(r'^accueil/$',views.IndexView.logout, name='accueil'),
    #url(r'^loggedin/$',),
    #url(r'^invalid/$',),
]

urlpatterns = format_suffix_patterns(urlpatterns)

#if settings.DEBUG:
#    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)