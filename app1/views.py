from django.shortcuts import render,HttpResponse
from app1.forms import regform, passform , forgetform

# Create your views here.
def port(request):
    return render(request,'porfolio.html')
def login(request):
    return render(request,'login.html')

def lostpsd(request):
    return HttpResponser('password lost') 
def terms(request):
    return render(request,'terms.html')
def privacy(request):
    return render(request,'privacy.html')
def register(request):
    
    if request.method== 'POST':
        fm=regform(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'password.html')
    else:
        fm = regform()
      
    return render(request,'register.html',{'reg': fm})
def verifypsd(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                return render(request,'home.html')  # Redirect to your home page or any other desired page
            else:
                messages.error(request, 'Invalid email or password.')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
def password(request):
    if request.method =='POST' :
        pf=passform(request.POST)
        if pf.is_valid():
            pf.save()
            return render(request,'password.html')
    else:
        pf=passform()   
    return render(request,'password.html',{'ps':pf})
def forget(request):
    if request.method =='POST':
        fog=forgetform(request.POST)
        if fog.is_valid():
            fog.save()
            return render(request,'forget.html')
    else:
        fog=forgetform()
    return render(request,'forget.html',{'fg':fog})
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')