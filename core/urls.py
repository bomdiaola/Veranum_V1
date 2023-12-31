from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('blog/', blog, name="blog"),
    path('contact/', contact, name="contact"),
    path('elements/', elements, name="elements"),
    path('rooms/', rooms, name="rooms"),
    path('indexAdmin/', indexAdmin, name="indexAdmin"),
]
