"""
Definition of urls for tutorial.
"""

from django.conf.urls import include, url
from rest_framework import routers
from quickstart import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', tutorial.views.home, name='home'),
    # url(r'^tutorial/', include('tutorial.tutorial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
