# from django.urls import path
# from . import views

# urlpatterns = [
#   path('members/', views.members, name='members'),
#   path('about-us/', views.aboutUs, name='aboutus')
# ]
from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about-us/', views.about, name='about'),
  path('contact-us/', views.contact, name='contact page')
]