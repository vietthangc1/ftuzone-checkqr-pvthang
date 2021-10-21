from django.urls import path
from . import views

app_name = "app"

urlpatterns = [
  path('customers/delete/<slug:pk>/', views.CustomerDeleteView.as_view(), name='customers_delete'),
  path('customers/', views.CustomerListView.as_view(), name="customers_list"),
  path('customers/create', views.CustomerCreateView.as_view(), name="customers_create"),
  path('scan/<slug:id>/', views.scan, name="scan"),
  path('login/', views.user_login, name='login'),
  path('logout/', views.user_logout, name='logout'),
  path('special/', views.special, name='special')
]