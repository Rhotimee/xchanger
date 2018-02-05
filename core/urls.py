from django.conf.urls import url
from .views import SbdCreateView, SbdList
from . import views

urlpatterns = [

    # url(r'^$', IndexView.as_view(), name='index'),
    url(r'^$', views.index_view, name='index'),
    url(r'^update/$', views.update_profile, name='update'),
    url(r'^sell/$', SbdCreateView.as_view(), name='create'),
]