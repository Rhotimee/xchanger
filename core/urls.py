from django.conf.urls import url
from .views import IndexView
from . import views

urlpatterns = [

    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView, name='index'),


]
