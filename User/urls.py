from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', login_view, name='login'),
    url(r'^logout', logout_view, name='logout'),
    url(r'^register/$', register_view, name='register'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^profile/change/$', change_profile_view, name='change_profile'),

]
