from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.views.generic import CreateView
from .form import CustomerRegisterForm, AppointmentForm
from .models import User,Client,Worker,Reservation
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.


def renderlogin(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except:
            pass
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('homepage')
    return render(request,"loginform.html",{'form':AuthenticationForm()})

def logoutuser(request):
    logout(request)
    return redirect("homepage")

def services(request):
    serv= ('Сardiology','Dentistry', 'Dermatology','Ophthalmology', 'Surgery')
    return render(request,"Services.html",{'serv' :serv})

def doctors(request,choice):
    doc=None
    if choice == 'Сardiology':
        doc=Worker.objects.filter(Specialisation='Cardiologist')
    if choice == 'Dentistry':
        doc=Worker.objects.filter(Specialisation='Dentist')
    if choice == 'Dermatology':
        doc=Worker.objects.filter(Specialisation='Dermatologist')
    if choice == 'Ophthalmology':
        doc=Worker.objects.filter(Specialisation='Ophthalmologist')
    if choice == 'Surgery':
        doc=Worker.objects.filter(Specialisation='Surgeon')
    return render(request,"doctors.html",{'doc':doc})

def renderregister(request):
    form = CustomerRegisterForm()
    if request.user.is_authenticated:
        return redirect("homepage")
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        user=form.save()
        login(request,user)
        return redirect('homepage')
    return render(request,"registerform.html",{'form': form})

def renderreservation(request,choice):
    doc = None
    doct = Worker.objects.all()
    for d in doct:
        if d.user.id== int(choice):
            doc=d
    form= AppointmentForm()
    if request.method == 'POST':
        client = Client.objects.get(user=request.user)
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save(client,doc)
            return redirect('homepage')
    return render(request, "reservationpage.html", {'doc': doc,'form':form})

def showreserv(request):
    worker= Worker.objects.get(user=request.user)
    reservations= Reservation.objects.filter(docid=worker)
    return render(request, "showreserv.html", {'reservations': reservations})