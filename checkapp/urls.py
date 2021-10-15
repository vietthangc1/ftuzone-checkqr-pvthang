from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
  path('delete/<slug:id>/', views.delete, name='delete'),
  path('showdtb/', views.showDTB, name="showdtb"),
  path('adddTB/', views.addDTB, name="adddtb"),
  path('scan/<slug:id>/', views.scan, name="scan"),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('special/', views.special, name='special')
]