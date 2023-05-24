from django.shortcuts import render, HttpResponse
from home.models import contact,join
from django.contrib.messages import constants as messages

def index(request):
    return render(request,'index.html')
    #return HttpResponse('This is home page')
def contacthi(request):
    if request.method=='POST':
       name = request.POST['name']
       email = request.POST['email']
       phone= request.POST['phone']
       issue= request.POST['issue']
       print(name, email, phone, issue)
       Contact= contact(name=name,email=email,phone=phone,issue=issue)
       Contact.save()
      
    return render(request,'contact.html')
    #return HttpResponse('This is contact this site')
def services(request):
    return render(request, 'services.html')    
def about(request):
    return render(request, 'about.html')    
def joinus(request):
    if request.method=='POST':
       names = request.POST['names']
       emails = request.POST['emails']
       describe= request.POST['describe']
       print(names, emails, describe)
       Join=join(names=names,emails=emails,describe=describe)
       Join.save()
    return render(request,'joinus.html')
