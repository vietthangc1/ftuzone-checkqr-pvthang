from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from checkapp.models import Customers
from .forms import CustomerForm
from .models import Customers
from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(req):
  try:
    render_dic = {'th_currentUser': currentUser}
    print(currentUser)
    return render(req, "checkapp/index.html", render_dic)
  except:
    return render(req, "checkapp/index.html")

def showDTB(req):
  data = Customers.objects.order_by("created_time")
  return render(req, "checkapp/showdtb.html", {"th_data": data})

@login_required
def addDTB(req):
  added = False
  form = CustomerForm()
  if req.method == "POST":
    form = CustomerForm(req.POST)
    if form.is_valid():
      print("VALIDATED")
      added = True
      form.save()
    else:
      print(form.errors)
  render_dic = {"th_form": form, "th_added": added}
  return render(req, "checkapp/adddtb.html", render_dic)

def scan(req, id):
  checkFirsttime = False
  try:
    result = get_object_or_404(Customers, user_id = id)
    if result.times_of_scan == 0:
      checkFirsttime = True
    new_times = result.times_of_scan + 1
    new_scan_date = datetime.today()
    Customers.objects.filter(user_id = id).update(times_of_scan = new_times, last_scanned = new_scan_date)   
  except:
    result = None
  return render(req, "checkapp/scan.html", {"th_data": result, "th_check": checkFirsttime})

def user_login(req):
  if req.method == "POST":
    username = req.POST.get("th_username")
    password = req.POST.get("th_password")

    global currentUser
    currentUser = authenticate(username=username, password=password)

    if currentUser:
      if currentUser.is_active:
        login(req, currentUser)
        return HttpResponseRedirect(reverse("index"))
      else:
        return HttpResponse("Not active")
    else:
      return HttpResponse("Wrong account. Check username: %s password: %s" %(username, password))
  else:
    return render(req, "checkapp/login.html")

@login_required
def user_logout(req):
  logout(req)
  return HttpResponseRedirect(reverse("index"))

@login_required
def delete(req, id):
  Customers.objects.filter(user_id=id).delete()
  return HttpResponseRedirect(reverse("app:showdtb"))

@login_required
def special(req):
  return HttpResponse("Logged in")