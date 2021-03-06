from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from core.views import (LoginView, HomeView, register_user, change_password, UpdateProfile, list_users, disable_user,
                        active_user, delete_user, EditProfile)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('user/disable/<int:pk>', disable_user, name='disable_user'),
    path('user/active/<int:pk>', active_user, name='active_user'),
    path('user/delete/<int:pk>', delete_user, name='delete_user'),
    path('user/edit/<int:pk>', EditProfile.as_view(), name='edit_user'),

    path('animals/', include('animal.urls')),
    path('events/', include('events.urls')),
    path('contacts/', include('contacts.urls')),
    path('expenses/', include('finance.urls')),
    path('donations/', include('donation.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url('login/', LoginView.as_view(), name='login'),
    url(r'user/register/$', register_user, name='create_user'),
    url(r'user/all/$', list_users, name='list_users'),
    url(r'profile/password/$', change_password, name='change_password'),
    url(r'profile/update/$', UpdateProfile.as_view(), name='update_profile'),

]
