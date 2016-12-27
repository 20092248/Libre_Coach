from django.conf.urls import include, url
from django.contrib import admin
from connection.views import goToForm, goToHome, addProjet
from projects.views import goToProjet
from profils.views import goToProfil
from disponibilite.views import goToDispo

urlpatterns = [
    # Examples:
    # url(r'^$', 'LibreCoach.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^index', goToForm, name='login'),
    url(r'^home', goToHome),
    url(r'^projet', goToProjet),
    url(r'^profil', goToProfil),
    url(r'^add/(\d{1})',addProjet),
    url(r'^add/(\d{2})',addProjet),
    url(r'^dispo', goToDispo),

]
