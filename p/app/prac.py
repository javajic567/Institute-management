def enq_view_decorator(func):
    def wrapper(request):
        if request.path == '/regis_view/':
            return redirect('enq_view')
        else:
            return func(request)

    return wrapper



@enq_view_decorator
def regis_view(request):
    if request.method == "POST":
        a = Regis_stu_form(request.POST)
        if a.is_valid():
            a.save()
            e=Enq.objects.get(mobile=request.POST['mobile'])
            e.delete()
            # fees=Regis_stu.objects.get(fees=request.POST['fees'])
            # paid_fees=Regis_stu.objects.get(paid_fees=request.POST['paid_fess'])
            #pendingfee=fees-paid_fees we are here in this regis_stu only right so no need to take like this
            name=request.POST['stu_name']
            mobile=request.POST['mobile']
            course=request.POST['course']
            fees=request.POST['fees']
            trainer_name=request.POST['trainer_name']
            paid_fees=request.POST['paid_fees']
            pendingfee=int(fees)-int(paid_fees)
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




