from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
  path('showdtb/', views.showDTB, name="showdtb"),
  path('adddTB/', views.addDTB, name="adddtb"),
  path('scan/<slug:id>/', views.scan, name="scan")
]