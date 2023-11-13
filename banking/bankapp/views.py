from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .forms import NewMemberForm
from .models import District, Branch, NewMember


# # Create your views here.
#
#
def person_create_view(request):
    form = NewMemberForm()
    if request.method == 'POST':
        # print(request.POST.get('materials'))
        form = NewMemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,"Application Accepted")
            return redirect('bankapp:person_add')
        else:
            messages.info(request,"Failed")
    return render(request,'form.html',{'form':form})



def home(request):
    district_list=District.objects.all()
    return render(request,'index.html',{'d_list':district_list})
    # return HttpResponse("hello")
def registration(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('bankapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
                return redirect('bankapp:login')
        else:
            messages.info(request,"Password not matching")
            return redirect('bankapp:register')
    return render(request,'register.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('bankapp:content')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('bankapp:login')
    return render(request,'login.html')

def content(request):
    # form = NewMemberForm()
    # if request.method == 'POST':
    #     form = NewMemberForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('content')
    #     else:
    #         return HttpResponse("Failed")
    # return render(request,'content.html',{'form':form})
    return render(request,'content.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

#ajax


def load_branches(request):

    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id)
    return render(request,'dropdown_list.html',{'branches':branches})