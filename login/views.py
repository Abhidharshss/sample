from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from. models import user as usr,login as log
from django.contrib.auth import logout
# Create your views here.

def login(request):
    print("login")
    msg=request.GET.get("msg","")
    if 'username' in request.session:
        return redirect('adminhome')
    return render(request,"login.html",{"msg":msg})

def adminhome(request):
    msg=request.GET.get("msg","")
    if 'username' in request.session:
        if 'q' in request.GET:
            q=request.GET['q']
            data=usr.objects.filter(firstname__icontains=q)
        else:
            data=usr.objects.all()
    else:
        return redirect("login")
    return render(request,"adminhome.html",{"msg":msg,"data":data})

def userreg(request):
    if request.POST:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        usr.objects.create(firstname=firstname,lastname=lastname,email=email,phone=phone,address=address)
        return redirect("/adminhome?msg=registration successfull")
    else:
        return redirect("/adminhome?msg=registration failed")

def logi(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        datac=log.objects.filter(username=username,password=password).count()
        if datac==1:
            data=log.objects.get(username=username,password=password)
            request.session['username'] = data.username
            request.session['password'] = data.password
            return redirect('/adminhome')
        else:
            return redirect('/login?msg=invalid username or password')
    else:
        return redirect('/login?msg=something went wrong')

def delusr(request):
    id=request.POST['uid']
    usr.objects.filter(userid=id).delete()
    return redirect("/adminhome?msg=deleted successfully")

def sample(request):
    data=usr.objects.all()
    return render(request,'sample.html',{"data":data})

def editusr(request):
    id=request.POST['uid']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    phone=request.POST['phone']
    address=request.POST['address']
    usr.objects.filter(userid=id).update(firstname=firstname,lastname=lastname,email=email,phone=phone,address=address)
    return redirect("/adminhome?msg=details updated")

def logoutfrom(request):
    del request.session['username']
    del request.session['password']
    response = HttpResponseRedirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Expires'] = '0'
    return response

        # del request.session['username']
        # del request.session['password']
        # response.delete_cookie(name)
        # return redirect('/login')
    