from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_new$', views.process_new),
    url(r'^password_dashboard$', views.password_dashboard),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add_password$', views.add_password),
    url(r'^password_added$', views.password_added),
    url(r'^delete/(?P<password_id>\d+)$', views.delete),
    url(r'^edit/(?P<password_id>\d+)$', views.edit),
    url(r'^on_edit_pass/(?P<password_id>\d+)$', views.on_edit_pass),
    url(r'^on_edit_user/(?P<user_id>\d+)$', views.on_edit_user),
    url(r'^profile$', views.profile),
    url(r'^mobile_display/(?P<password_id>\d+)$', views.mobile_display),

    url(r'^logout$', views.logout)

]