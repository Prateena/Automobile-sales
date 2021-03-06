"""Automobile_sales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from myapp.api import views
from django.core.urlresolvers import reverse


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'userprofile',views.UserProfileViewSet)
router.register(r'vehicles', views.VehicleViewSet)


urlpatterns = [
	# url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('myapp.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    # url(r'^api/automobile/',include("myapp.api.urls",namespace='automobile-api') ),
    
    # url(r'^myapp/',include('myapp.urls'),)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
