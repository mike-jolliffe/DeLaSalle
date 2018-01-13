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
    url(r'corporate_signup/$', page_views.corporate_signup, name='corporate_signup'),
    url(r'check_promo/$', page_views.check_promo, name='check_promo'),
    url(r'register_teams/$', page_views.register_teams, name='register_teams'),
    url(r'support/$', page_views.support, name='support'),
    url(r'support/addSupporter', page_views.addSupporter, name='addSupporter'),
    url(r'leaderboard/$', page_views.leaderboard, name='leaderboard'),
    url(r'contact_us/$', page_views.contact_us, name='contact_us')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

