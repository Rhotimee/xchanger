from django.conf.urls import url
from .views import index_view, update_profile
from . import views

urlpatterns = [

    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', views.index_view, name='index'),
    url(r'^update/$', views.update_profile, name='update'),


]
