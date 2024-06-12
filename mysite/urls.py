from django.urls import path
from django.contrib.auth import views
from django.views.generic.base import RedirectView

from django.conf import settings
from django.conf.urls.static import static

import BastianWorld.forms
import BastianWorld.views

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('', include('BastianWorld.urls')),
    path('', BastianWorld.views.gallery, name='gallery'),
    path('favicon.ico', RedirectView.as_view(url='/static/icons/favicon.ico', permanent=True)),
    path('<slug:slug>', BastianWorld.views.AlbumDetail.as_view(), name='album'),
    # Auth related urls

    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),

     # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
