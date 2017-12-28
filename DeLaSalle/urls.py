from django.conf.urls import url
from django.contrib import admin
from pages import views as page_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', page_views.home, name='home'),
    url(r'register/$', page_views.register, name='register'),
    url(r'add_registrant/$', page_views.add_registrant, name='add_registrant'),
    url(r'sponsor/$', page_views.sponsor, name='sponsor'),
    url(r'sponsor/opportunities$', page_views.opportunities, name='opportunities'),
    url(r'support/$', page_views.support, name='support'),
    url(r'support/addSupporter', page_views.addSupporter, name='addSupporter'),
    url(r'leaderboard/$', page_views.leaderboard, name='leaderboard'),
    url(r'contact_us/$', page_views.contact_us, name='contact_us')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

