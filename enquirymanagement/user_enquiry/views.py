import email
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserDatabase,EnquiryDatabase

def userClick(req):
	return render(req,"userclick.html")

def userReg(req):
	return render(req,"ureg.html")

def userLogin(req):
	return render(req,"ulog.html")

def uregistration(req):
    if req.method=='POST':
        fnm=req.POST.get('fname')
        lnm=req.POST.get('lname')
        em=req.POST.get('email')
        cn=req.POST.get('contact')
        pwd1=req.POST.get('password')
        pwd2=req.POST.get('cpassword')
        user=UserDatabase.objects.filter(Email=em)
        if user:
            msg="User already exits"
            return render(req,"ureg.html",{'msg':msg})
        else:
            if pwd1==pwd2:
                newuser=UserDatabase(Firstname=fnm,Lastname=lnm,Email=em,Contact=cn,Password=pwd1)
                newuser.save()
                msg="User registerd successfully"
                return render(req,"ulog.html",{'umsg':msg})
            else:
                msg="Password doesn't match"
                return render(req,"ureg.html",{'msg':msg})
    
        
def ulogin(req):
	if req.method=="POST":
		em=req.POST.get('email')
		pwd1=req.POST.get('password')
		try:
			newuser=UserDatabase.objects.get(Email=em)
			if newuser.Password==pwd1:
				req.session['Firstname']=newuser.Firstname
				req.session['Lastname']=newuser.Lastname
				return render(req,"uafterlogin.html")
			else:
				msg="Invalid Password"
				return render(req,"ulog.html",{'msg':msg})
		except UserDatabase.DoesNotExist:
			msg="User does not exits"
			return render(req,"ureg.html",{'msg':msg})

def uafterlogin(req):
	return render(req,"uafterlogin.html")

def uenquiryform(req):
	return render(req,"uenquiryform.html")

def uenquiryTask(req):
	if req.method=="POST":
		nm=req.POST['name']
		em=req.POST['email']
		cn=req.POST['contact']
		add=req.POST['address']
		qur=req.POST['query']
		data=EnquiryDatabase(Name=nm,Email=em,Contact=cn,Address=add,Query=qur)
		data.save()
		emsg="Your query sent successfully"
	return render(req,"uenquiryform.html",{'emsg':emsg})

def DisplayAdmin(req):
	enqdata=EnquiryDatabase.objects.all()
	return render(req,"displayadmin.html",{'enqdata':enqdata})

def deletedata(req,id):
	data=EnquiryDatabase.objects.get(pk=id)
	data.delete()
	return redirect('/user/DisplayAdmin')


def updatedata(req,id):
	if req.method=="POST":
		nm=req.POST['name']
		em=req.POST['email']
		cn=req.POST['contact']
		add=req.POST['address']
		qur=req.POST['query']
		data=EnquiryDatabase(id=id,Name=nm,Email=em,Contact=cn,Address=add,Query=qur)
		data.save()
		return redirect('/user/DisplayAdmin')
	data=EnquiryDatabase.objects.get(pk=id)
	return render(req,"update.html",{'data':data})


#	email=rec.values()[0].get('Email')

# def myenq(req):
# 	email=newuser.values()[0].get('Email')
# 	print(email)
# 	data=EnquiryDatabase.objects.get(Email=email)
# 	return render(req,"viewenq.html",{'i':data})
