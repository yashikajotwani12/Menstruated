from django.urls import path
from Home import views
app_name='Home'

urlpatterns = [
  
  path('', views.index, name='home'),
  path('contact', views.contact, name ="contact"),
  path('faq', views.faq, name ="faq"),
  path('pcod', views.pcod, name ="pcod"),
  path('selfcare', views.selfcare, name ="selfcare"),

  
]

