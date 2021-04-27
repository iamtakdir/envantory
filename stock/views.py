from django.shortcuts import render ,redirect
from .models import *
from .forms import *
from .filters import Filter
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users

# Create your views here.

@login_required(login_url='user_login')
def home (request):

    return render(request, 'stock/home.html')

@login_required(login_url='user_login')
def list_items(request):

    items = Stock.objects.all()
    supplier=Supplier.objects.all()

    total_items= items.count()
    total_supplier = supplier.count()
    total_quantity=[]
    
    for item in items:

        total_quantity.append(item.quantity)
    total_quantity=sum(total_quantity)


    search= Filter(request.GET, queryset=items)

    items = search.qs
    
    

    context = {
    
    'items':items,
    'search':search,
    'total_items':total_items,
    'total_supplier':total_supplier,
    'total_quantity':total_quantity
    }

    return render (request, 'stock/itmes.html', context)

@login_required(login_url='user_login')
def add_stock_form (request):
    form = Add_stock_form(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Added Stock')
        return redirect('list_items')

    context = {
        'form': form 
    }

    return render (request,'stock/add_stock.html',context)

@login_required(login_url='user_login')
def add_sup_form (request):

    form = Add_Sup_form(request.POST or None)

    if form.is_valid():
        form.save()
        
        messages.success(request, 'Successfully Added Supplier')
        return redirect('list_items')
        

    context = {
        'form': form 
    }

    return render (request,'stock/add_sup.html',context)


@login_required(login_url='user_login')
def add_catrgory_form (request):

    form = Add_Category_form(request.POST or None)

    if form.is_valid():
        form.save()
        
        messages.success(request, 'Successfully Added Category')
        return redirect('list_items')
        

    context = {
        'form': form 
    }

    return render (request,'stock/add_category.html',context)


@login_required(login_url='user_login')
def Update_stock_form (request,pk):
    items = Stock.objects.get(id=pk)

    form = Add_stock_form(instance=items)

    if request.method=='POST':

        form = Add_stock_form(request.POST,instance=items)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Updated Stock')
            return redirect('list_items')

    context ={
        'form' : form 
    }

    return render (request,'stock/update_stock.html',context)

@login_required(login_url='user_login')
@allowed_users(allowed_roles=['admin'])
def delete_stock(request, pk):
    item = Stock.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Successfully Deleted Stock')
        return redirect('list_items')
    return render(request, 'stock/delete_stock.html')


@login_required(login_url='user_login')
def stock_details (request, pk):

    item = Stock.objects.get(id=pk)

    print (item.supplier.sup_mobile)

    context={
        'item':item
    }

    return render (request, 'stock/stock_details.html',context)

@login_required(login_url='user_login')
def total_list(request):

    items = Stock.objects.all()
    suppliers = Supplier.objects.all()
    categories= Category.objects.all()

 

    context ={
        'items':items ,
        'suppliers':suppliers,
        'categories':categories
    }

    return render (request, 'stock/total_list.html', context)

@login_required(login_url='user_login')
def logoutuser (request):

    if request.method == 'POST':
        logout(request)
        return redirect('list_items')
    
