from .models import User
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    context={'all_ninjas':User.objects.all()}
    return render(request,'user_dash.html',context)

def add(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST["first_name"],last_name= request.POST["first_name"],email_address= request.POST["Email"],age=request.POST["Age"])
    return redirect("/")