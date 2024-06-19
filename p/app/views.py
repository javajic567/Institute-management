from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import Regis_stu_form, Enq_form, User_regis_form
from .models import Regis_stu, Enq, PendingFee


# Create your views here.

def h(request):
    return render(request,'base1.html')

@login_required(login_url='LI')
def enq_view(request):
    if request.method == "POST":
        b = Enq_form(request.POST)
        if b.is_valid():
            b.save()
            return redirect("Enquiry")
        else:
            return HttpResponse("enquiry not successful")
    else:
        obj = Enq_form()
        return render(request, 'enq.html', {'obj': obj})

def enq_view_decorator(func):
    def wrapper(request):
        if request.path == '/registration/':
            return redirect('Enquiry')
        else:
            return func(request)

    return wrapper
@login_required(login_url='LI')
def regis_view(request):
    if request.method == "POST":
        a = Regis_stu_form(request.POST)
        if a.is_valid():
            name = request.POST['stu_name']
            mobile = request.POST['mobile']
            course = request.POST['course']
            age = request.POST['age']
            address = request.POST['address']

            fees = request.POST['fees']
            trainer_name = request.POST['trainer_name']
            paid_fees = request.POST['paid_fees']
            pendingfee = int(fees) - int(paid_fees)
            b=Regis_stu(stu_name=name,mobile=mobile,age=age,address=address,course=course,fees=fees,paid_fees=paid_fees,trainer_name=trainer_name)

            b.save()
            try:
              e=Enq.objects.get(mobile=request.POST['mobile'])
              e.delete()
            except ObjectDoesNotExist:
                e = None
            # fees=Regis_stu.objects.get(fees=request.POST['fees'])
            # paid_fees=Regis_stu.objects.get(paid_fees=request.POST['paid_fess'])
            #pendingfee=fees-paid_fees we are here in this regis_stu only right so no need to take like this

            if pendingfee<=0:
                return redirect('display')
            else:
                obj=PendingFee(stu_name=name,mobile=mobile,course=course,fees=fees,trainer_name=trainer_name,paid_fees=paid_fees,pendingfee=pendingfee)
                obj.save()
                obj1=PendingFee.objects.all()

                return render(request,'pf.html',{'obj1':obj1})

        else:
            print(a.errors)
            return HttpResponse("registration is  not successful")
    else:
        obj = Regis_stu_form()
        return render(request, 'regis.html', {'obj': obj})
@login_required(login_url='LI')
def pf_view(request):
    obj1 = PendingFee.objects.all()
    return render(request, 'pf.html', {'obj1': obj1})

@login_required(login_url='LI')
def Display_enq(request):
    obj=Enq.objects.all()
    return render(request,'Dis_enq.html',{'obj':obj})

def pay_view(request,pk):
    if request.method == 'POST':
        p = PendingFee.objects.get(id=pk)
        p.delete()
        return redirect('Pendingfees')

    else:
        obj = PendingFee.objects.get(id=pk)
        return render(request, 'pay.html', {'obj': obj})
def user_regis_view(request):
    if request.method=='POST':
        c=User_regis_form(request.POST)
        if c.is_valid():
            c.save()
            return redirect('LI')
        else:
            return HttpResponse("registration not successful")
    else:
        obj=User_regis_form()
        return render(request,"UserR.html",{"obj":obj})

def static_view(request):
    return render(request,"static_file.html")