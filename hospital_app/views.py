from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'base.html')

@login_required(login_url="/login")
def add_drug(request):
    context = {"drug_type" : d_type.objects.all()}
    if request.method == "POST":
        table = drug()
        table.drug_name = request.POST['drug_name']
        table.drug_type = d_type.objects.get(type_id = request.POST['drug_type'])
        table.drug_qty = request.POST['drug_qty']
        table.drug_exp = request.POST['drug_expired']
        table.save()
        return redirect('/manage_drug')
    return render(request,'add_drug.html',context)

@login_required(login_url="/login")
def add_type(request):
    if request.method == "POST":
        table = d_type()
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'add_type.html')

def manage_drug(request):
    show_drug = drug.objects.all()
    context  = {"drug" : show_drug}
    return render(request,'edit_drug.html',context)

def manage_type(request):
    show_type = d_type.objects.all()
    context  = {"type" : show_type}
    return render(request,'manage_type.html',context)

@login_required(login_url="/login")
def delete_drug(request,pk):
    table = drug.objects.get(drug_id=pk)
    table.delete()
    return redirect('/manage_drug')

@login_required(login_url="/login")
def delete_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    table.delete()
    return redirect('/manage_type')

@login_required(login_url="/login")
def edit_drug(request,pk):
    table = drug.objects.get(drug_id=pk)
    table2 = d_type.objects.all()
    context = {"drug_data" : table , "drug_type" : table2}
    if request.method == "POST":
        table.drug_name = request.POST['drug_name']
        table.drug_type = d_type.objects.get(type_id = request.POST['drug_type'])
        table.drug_qty = request.POST['drug_qty']
        table.drug_exp = request.POST['drug_expired'] 
        table.save()
        return redirect('/manage_drug')
    return render(request,'edit_d.html',context)

@login_required(login_url="/login")
def edit_type(request,pk):
    table = d_type.objects.get(type_id=pk)
    context = {"type_data" : table}
    if request.method == "POST":
        table.type_name = request.POST['type_name']
        table.save()
        return redirect('/manage_type')
    return render(request,'edit_t.html',context)

@login_required(login_url="/login")
def increase_drug(request,pk):
    print (pk)
    table = drug.objects.get(drug_id=pk)
    update_qty = table.drug_qty+1
    table.drug_qty = update_qty
    table.save()
    return redirect('/manage_drug') 

@login_required(login_url="/login")
def decrease_drug(request,pk):
    print (pk)
    table = drug.objects.get(drug_id=pk)
    update_qty = table.drug_qty+1
    table.drug_qty = update_qty
    table.save()
    return redirect('/manage_drug') 

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('/manage_drug')
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
            pass
    return render(request, 'login.html')

def logout_view(request):
        logout(request)
        return render(request, 'login.html')