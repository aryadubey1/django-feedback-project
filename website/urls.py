from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    # path('fix-admin-access-9988/', views.create_emergency_admin)
]

