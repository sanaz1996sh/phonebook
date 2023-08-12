from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
      return render(request,"information_app/home.html")
     
   
def office(request):
    return render(request,"information_app/welcome.html")
    
  
def info(request,name):
    l=[
        {"name_org":"fani","name_office":"اداره فنی و حرفه ای","phone_office":"32228046-038","web_office":"https://ctvto.ir"},
        {"name_org":"kar","name_office":"اداره کار","phone_office":"32253360-038","web_office":"http://chmb.mcls.gov.ir"},
        {"name_org":"uni","name_office":"دانشگاه شهرکرد","phone_office":"32324401-038","web_office":"http://sku.ac.ir"},
        {"name_org":"tamin","name_office":"اداره تامین اجتماعی","phone_office":"32245492-038","web_office":"http://chb.tamin.ir"},    
    ]
    for i in l :
        if (name==i["name_org"]) :
             return render(request,"information_app/showinfo.html",context=i)
    return render(request,"information_app/error.html")    



