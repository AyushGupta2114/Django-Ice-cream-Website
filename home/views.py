from django.shortcuts import render, HttpResponse
# Create your views here.
def index(request):
    context={
        'variable1':"Ayush is great",
        'variable2':"Rohan is great"
    }
    return render(request,'index.html',context)

def about(request):
    # return HttpResponse("This is about page")
     return render(request,'about.html')

def services(request):
    # return HttpResponse("This is services page")
     return render(request,'services.html')

def contact(request):
    # return HttpResponse("This is contact page")
     return render(request,'contact.html')
