from django.shortcuts import render , redirect
from Admin_App.models import CategoryDB, ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from WebApp.models import ContactDB


# Create your views here.

def Dashboard(request):
    categories = CategoryDB.objects.count()
    product = ProductDB.objects.count()
    return render(request,'Dashboard.html' , {'categories' : categories , 'product': product} )

def add_categories(request):
    return render(request,'Add_Categories.html')

def save_category(request):
    if request.method=="POST":
        c = request.POST.get('category')
        i = request.FILES['image']
        d = request.POST.get('category_description')
        obj = CategoryDB(Category_Name=c,Category_Image=i,Category_Description=d)
        obj.save()
        messages.success(request , 'Category saved successfully')
        return redirect(add_categories)

def view_category(request):
    category = CategoryDB.objects.all()
    return render(request, 'Category_Details.html', {'category': category})

def edit_category(request , Category_ID):
    data = CategoryDB.objects.get(id=Category_ID)
    return render(request, 'Edit_Category.html', {'data': data})

def update_category(request,Category_ID):
    if request.method == "POST":
        c = request.POST.get('category')
        d = request.POST.get('category_description')
    try:
        i =request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(i.name,i)
    except MultiValueDictKeyError :
        file = CategoryDB.objects.get(id=Category_ID).Category_Image
    CategoryDB.objects.filter(id=Category_ID).update(Category_Name=c,Category_Image=file,Category_Description=d)
    messages.success(request, 'Category Updated')
    return redirect(view_category)


def delete_category(request,C_ID):
    Category=CategoryDB.objects.filter(id=C_ID)
    Category.delete()
    messages.success(request, 'Category Deleted')
    return redirect(view_category)


# *********************************************** #

def add_product(request):
    categories = CategoryDB.objects.all()
    return render(request , 'Add_Product.html' , {'categories' : categories})

def save_product(request):
    if request.method=="POST":
        c = request.POST.get("product_category")
        n = request.POST.get("product_name")
        p = request.POST.get("price")
        d = request.POST.get("product_description")
        i = request.FILES["image"]
        obj = ProductDB(Category_Name=c,Product_Name=n,Product_Description=d,Price=p,Product_Image=i)
        obj.save()
        messages.success(request, 'Product saved successfully')
        return redirect(add_product)

def view_product(request):
        product = ProductDB.objects.all()
        return render(request, 'Product_Details.html', {'product': product})

def edit_product(request , Product_ID):
    data = ProductDB.objects.get(id=Product_ID)
    categories = CategoryDB.objects.all()
    return render(request, 'Edit_Product.html', {'data': data,'categories' : categories })

def update_product(request,Product_ID):
    if request.method == "POST":
        c = request.POST.get("product_category")
        n = request.POST.get("product_name")
        p = request.POST.get("price")
        d = request.POST.get("product_description")
    try:
        i =request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(i.name,i)
    except MultiValueDictKeyError :
        file = ProductDB.objects.get(id=Product_ID).Product_Image
    ProductDB.objects.filter(id=Product_ID).update(Category_Name=c,Product_Name=n,Product_Description=d,Price=p,Product_Image=file)
    messages.success(request, 'Product Updated')
    return redirect(view_product)

def delete_product(request,P_ID):
    Product=ProductDB.objects.filter(id=P_ID)
    Product.delete()
    messages.success(request, 'Product deleted')
    return redirect(view_product)

# **************************************** #

def admin_login_page(request):
    return render(request , 'Admin_Login.html')

def admin_login(request):
    if request.method=="POST":
        u_name = request.POST.get('username')
        p = request.POST.get('password')
        if User.objects.filter(username__contains=u_name).exists():
            x = authenticate(username = u_name , password = p)
            if x is not None:
                login(request , x)
                request.session['username'] = u_name
                request.session['password'] = p
                messages.success(request, 'Welcome to Natures Delight Admin Dashboard')
                return redirect(Dashboard)
            else :
                messages.warning(request, 'Invalid Password')
                return redirect(admin_login_page)
        else:
            messages.warning(request, 'Please login ')
            return redirect(admin_login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page)

#*****************************************************#

def contact_details(request):
    data = ContactDB.objects.all()
    return  render(request , 'Contact_Details.html', {'data' : data})

def delete_contact(request,Contact_ID):
    contact = ContactDB.objects.filter(id=Contact_ID)
    contact.delete()
    return redirect(contact_details)














