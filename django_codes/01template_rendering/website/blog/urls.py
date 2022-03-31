from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/contact/
# http://127.0.0.1:8000/about

urlpatterns = [
    path('',views.home,name="home"),
    path("about/",views.about,name="about"),
    path("contact/",views.contact,name="contact"),
    
]
