from django.conf.urls import url
from django.contrib import admin
from pages import views as page_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', page_views.home, name='home'),
    url(r'register/$', page_views.register, name='register'),
    url(r'donate/$', page_views.donate, name='donate'),
    url(r'leaderboard/$', page_views.leaderboard, name='leaderboard')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

