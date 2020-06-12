from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include('allauth.urls')),
    path("signup", views.signup, name='signup'),
    path('post', views.post, name='post'),
    path('postmore', views.postmore, name='postmore'),
    path('links', views.links, name='links'),
    path('places', views.places, name='places'),
    path('maulana', views.maulana, name='maulana'),
    path('contact', views.contactt, name='contact'),
    path('volunteer', views.volunteer, name='volunteer'),
    path('eventdetail/<int:post_id>', views.eventdetail, name='eventdetail'),
]