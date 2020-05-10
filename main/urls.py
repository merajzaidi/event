from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("signup", views.signup, name='signup'),
    path('post', views.post, name='post'),
    path('links', views.links, name='links'),
    path('places', views.places, name='places'),
    path('maulana', views.maulana, name='maulana'),
]