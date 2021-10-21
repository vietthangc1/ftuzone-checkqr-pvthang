from django.db import models
from datetime import datetime
import uuid
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.urls import reverse

# Create your models here.
class Customers(models.Model):
  user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=256)
  CardId = models.CharField(max_length=20, blank=True)
  YearofBirth = models.CharField(blank=True, max_length=4)
  email = models.EmailField(default="@gmail.com")
  phone = models.CharField(max_length=15, blank=True)
  school = models.CharField(max_length=256)
  created_time = models.DateTimeField(default=datetime.now, editable=False)
  times_of_scan = models.IntegerField(default=0, editable=False)
  last_scanned = models.DateTimeField(default=datetime.now, editable=False)

  @property
  def qr_link_local(self):
      "Returns the link of qr code for user_id."
      return "http://127.0.0.1:8000/app/scan/"+str(self.user_id)
      
  @property
  def qr_link_heroku(self):
      "Returns the link of qr code for user_id."
      return "http://vietthangc1.pythonanywhere.com/app/scan/"+str(self.user_id)

  def get_absolute_url(self):
    return reverse("app:customers_list")

  def __str__(self):
    return self.name+"-"+self.YearofBirth+"-"+self.school

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username