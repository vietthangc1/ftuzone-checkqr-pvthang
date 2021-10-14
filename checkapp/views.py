from django.shortcuts import render, get_object_or_404

from checkapp.models import Customers
from .forms import CustomerForm
from .models import Customers
from datetime import datetime

# Create your views here.
def index(req):
  return render(req, "checkapp/index.html")

def showDTB(req):
  data = Customers.objects.all()
  return render(req, "checkapp/showdtb.html", {"th_data": data})

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
