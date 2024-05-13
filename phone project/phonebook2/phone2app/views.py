from django.shortcuts import render
from.models import Phonebook

# Create your views here.

def fun1(request):
    return render(request,('index.html'))

def home(request):
    return render(request,'home1.html')

def insert(request):
    return render(request,'home2.html')

def update(request):
    return render(request,'home.html')


def addphone(request):
    emplis={}
    try:
        Name=request.POST['name']
        Phone=int(request.POST['phone'])
        phlist=Phonebook.objects.filter(name=Name)
        if phlist.exists():
            emplis['key']= "allready exists"
            return render(request,"home2.html",emplis)
        else:
            phlist=Phonebook(name=Name,phone=Phone)
            phlist.save()
        emplis['key']="phonenumber is added"
        return render(request,"home2.html",emplis)
    except Exception as b:
        print(b)
        emplis['key']= "phone number is not added"
        return render(request,"home2.html",emplis)
    
def display(request):
    disp=Phonebook.objects.all()
    return render(request,"home1.html",{'phn': disp})

    
def update2(request):
    try:
        oldname = request.POST['oldname']
        newname = request.POST['newname']
        newphonenumber = request.POST['newnum']
        if oldname == newname:
            return render(request, "home.html", {'key': 'Already exists'})
        contact = Phonebook.objects.get(name=oldname)
        if newname=='':
            contact.name = oldname
            contact.phone = newphonenumber
            contact.save()
        else:
            contact.name = newname
            contact.phone = newphonenumber
            contact.save()

        return render(request, "home.html", {'key': 'Updated'})
    except Phonebook.DoesNotExist:
        return render(request, "home.html", {'key': 'Contact not found'})
    except Exception as e:
        print(e)
        return render(request, "home.html", {'key': 'Not updated'})



def delete(request):
    try:
        dlt=request.POST['dlt']
        Phonebook.objects.filter(name=dlt).delete()
        return render(request,"home.html",{'del':'deleted'})
    except Exception as b:
        print(b)
        return render(request,"home.html",{'del':'not deleted '})
    
def home2(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')





