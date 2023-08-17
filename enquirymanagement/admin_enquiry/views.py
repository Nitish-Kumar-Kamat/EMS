from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import AdminDatabase

def adminClick(req):
    return render(req,'adminClick.html')

def adminReg(req):
    return render(req,'areg.html')

def adminLogin(req):
    return render(req,'alog.html')

def aregistration(req):
    if req.method=='POST':
        fnm=req.POST.get('fname')
        lnm=req.POST.get('lname')
        em=req.POST.get('email')
        cn=req.POST.get('contact')
        pwd1=req.POST.get('password')
        pwd2=req.POST.get('cpassword')
        user=AdminDatabase.objects.filter(Email=em)
        if user:
            msg="Admin already exits"
            return render(req,"areg.html",{'msg':msg})
        else:
            if pwd1==pwd2:
                newuser=AdminDatabase(Firstname=fnm,Lastname=lnm,Email=em,Contact=cn,Password=pwd1)
                newuser.save()
                msg="Admin registerd successfully"
                return render(req,"alog.html",{'amsg':msg})
            else:
                msg="Password doesn't match"
                return render(req,"areg.html",{'msg':msg})
    
        
def alogin(req):
    if req.method=='POST':
        em=req.POST['email']
        pwd1=req.POST['password']
        try:
            newuser=AdminDatabase.objects.get(Email=em)
            if newuser.Password==pwd1:
                req.session['Firstname']=newuser.Firstname
                req.session['Lastname']=newuser.Lastname
                return render(req,"aAfterlogin.html")
            else:
                msg="Invalid Password"
                return render(req,"alog.html",{'msg':msg})
        except AdminDatabase.DoesNotExist:
            msg="Admin does not exits"
            return render(req,"areg.html",{'msg':msg})


def aAfterlogin(req):
    return render(req,"aAfterlogin.html")
