from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .forms import *
from .models import *

def index(request):
    return render(request,'index.html',{'messages':Message.objects.filter(user='zidani')})

class SignupView(CreateView):
    model = User
    template_name = 'auth/signup.html'
    form_class = SignupForm
    def form_valid(self, form):
        login(self.request, form.save())
        return redirect('/')

def Logout(request):
    logout(request)
    return render(request,'auth/logout.html')

class Search(ListView):
    model = Message
    template_name = 'search.html'
    context_object_name = 'messages'
    def get_queryset(self):
        search = self.request.GET['search']
        return Message.objects.filter(message__icontains=search)

class Update(UpdateView):
    model = Message
    fields = ['message','pdf']
    template_name = 'update.html'
    success_url = '/'
    
def delete(request,id):
    if request.user.username == 'zidani':
        item = Message.objects.get(id=id)
        if request.method == 'POST':
            item.delete()
            return redirect('/')
        return render(request,'delete.html',{'item':item})
    else: 
        return redirect('/')

def add(request):
    if request.user.username == 'zidani':
        if request.method == 'POST':
            message = request.POST.get('message')
            pdf = request.FILES.get('pdf')
            data = Message(message=message,pdf=pdf,user=request.user)
            if pdf is None and message is None:
                return redirect('/add/')
            else:
                data.save()
                return redirect('/')
        return render(request, 'add.html')
    else:
        return redirect('/')
            