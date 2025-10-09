from django.shortcuts import render , redirect
from Admin_App.models import CategoryDB , ProductDB
from WebApp.models import RegistrationDB ,ContactDB , CartDB , OrderDB
from django.contrib import messages
from WebApp.decorators import session_login_redirect
import razorpay
from .models import NewsletterSubscriber

# Create your views here.
def Home(request):
    cart_total = 0
    user_name = request.session.get('Name')                                           # user_name a variable
    if user_name :                                                                    # Session name below in Name
        cart_total = CartDB.objects.filter(UserName = user_name).count
    categories = CategoryDB.objects.all()
    return render(request,'HomePage.html',{'categories' : categories,'cart_total': cart_total})

def all_products(request):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()
    product = ProductDB.objects.all()
    return render(request , 'All_products.html' , {'product' : product ,'categories' :categories ,
                                                   'cart_total' : cart_total})

def single_product(request,product_id):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()
    product = ProductDB.objects.get(id=product_id)
    return render(request , 'Single_Product.html',{'product' : product,'cart_total':cart_total,''
                                                                                               'categories':categories})

def filtered_product(request,ctg_name):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()
    current_category = CategoryDB.objects.get(Category_Name=ctg_name)
    product = ProductDB.objects.filter(Category_Name=ctg_name)
    return render(request , 'Filtered_Product.html' , {'current_category':current_category,'product' : product ,'cart_total':cart_total,
                                                                                               'categories':categories})

#**********************************************************#

def about_us(request):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()
    return render(request , 'About_Us.html',{'categories' :categories , 'cart_total' : cart_total})

def contact_us(request):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()
    return render(request , 'Contact_Us.html',{'categories' :categories , 'cart_total' : cart_total})

def save_contact_page(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        s = request.POST.get('subject')
        m = request.POST.get('message')
        obj = ContactDB(Name=n,E_Mail=e,Subject=s,Message=m)
        obj.save()
        messages.success(request, 'Message Send Successfully')
        return redirect(contact_us)


#*****************************************************#

def user_registration(request):
    return render(request , 'User_Registration.html')

def save_user_reg(request):
    if request.method=="POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        p1 = request.POST.get('password')
        p2 = request.POST.get('c_password')
        obj = RegistrationDB(Name=n,E_Mail=e,Password=p1,C_Password=p2)
        obj.save()
        messages.success(request, 'User Registered Successfully')
        return redirect(user_registration)

def user_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        p = request.POST.get('password')
        if RegistrationDB.objects.filter(Name=un,Password=p).exists():
            request.session['Name']=un
            request.session['Password']=p
            return redirect(Home)
        else :
            messages.success(request, 'Check Username and password')
            return redirect(user_registration)
    else :
        return redirect(user_registration)

def user_logout(request):
    del request.session['Name']
    del request.session['Password']
    return redirect(Home)


#*****************************************************#

def cart_page(request):
    categories = CategoryDB.objects.all()
    data =  CartDB.objects.filter(UserName=request.session['Name'])
    cart_total = 0
    user_name = request.session.get('Name')                                                  # user_name a variable
    if user_name:                                                                    # Session name below in Name
        cart_total = CartDB.objects.filter(UserName=user_name).count


        # Total Amount Calculation
        sub_total = 0
        delivery_charge = 0
        total_amount = 0
        data = CartDB.objects.filter(UserName=request.session['Name'])
        for i in data :
            sub_total += i.TotalPrice
            if sub_total > 500:
                delivery_charge = 50
            else :
                delivery_charge = 100
            total_amount = sub_total + delivery_charge

    return render(request , 'Cart.html' , {'data' : data ,'sub_total' : sub_total ,
                                         'delivery_charge' : delivery_charge, 'total_amount' : total_amount ,
                                           'categories' :categories , 'cart_total' : cart_total})

@ session_login_redirect
def save_to_cart(request):
    if request.method == "POST":
        username = request.POST.get('user_name')
        product_name = request.POST.get('product_name')
        qty = int(request.POST.get('quantity'))
        price = float(request.POST.get('price'))
        total = float(request.POST.get('total_price'))

        existing_cart_item = CartDB.objects.filter(UserName=username, ProductName=product_name)

        if existing_cart_item.exists():
            cart_item = existing_cart_item.first()
            cart_item.Quantity += qty
            cart_item.TotalPrice = cart_item.Quantity * cart_item.Price
            cart_item.save()

            if existing_cart_item.count() > 1:
                existing_cart_item.exclude(id=cart_item.id).delete()
        else:
            product = ProductDB.objects.filter(Product_Name=product_name).first()
            img = product.Product_Image if product else None

            obj = CartDB(
                UserName=username,
                ProductName=product_name,
                Quantity=qty,
                Price=price,
                TotalPrice=total,
                Product_Image=img
            )
            obj.save()
        return redirect(Home)

@ session_login_redirect
def update_cart_item(request,  Item_ID):
    if request.method=="POST":
        qty = request.POST.get('action')
        try :
            cart_item = CartDB.objects.get(id=Item_ID)
            if qty == "increase" :
                cart_item.Quantity += 1
            elif qty == "decrease" :
                if cart_item.Quantity > 1 :
                    cart_item.Quantity -= 1
                else :
                    cart_item.delete()   # remove from cart if quantity is zero
                    return redirect(cart_page)

            cart_item.TotalPrice = cart_item.Quantity * cart_item.Price
            cart_item.save()
        except  CartDB.DoesNotExist:
            pass
    return redirect(cart_page)

def cart_item_delete(request,Item_ID):
    data = CartDB.objects.filter(id=Item_ID)
    data.delete()
    return redirect(cart_page)

def checkout(request):
    cart_total = 0
    user_name = request.session.get('Name')                   # user_name a variable
    if user_name:                                             # Session name below in Name
        cart_total = CartDB.objects.filter(UserName=user_name).count
    categories = CategoryDB.objects.all()


    sub_total = 0
    delivery_charge = 0
    total_amount = 0
    data = CartDB.objects.filter(UserName=request.session['Name'])
    for i in data:
        sub_total += i.TotalPrice
        if sub_total > 500:
            delivery_charge = 50
        else:
            delivery_charge = 100
        total_amount = sub_total + delivery_charge
    return render(request,'CheckOut.html', {'categories' : categories,
                                            'cart_total': cart_total,'sub_total' : sub_total ,
                                         'delivery_charge' : delivery_charge, 'total_amount' : total_amount })


def save_checkout(request):
    if request.method=="POST":
        f_name = request.POST.get('f_name')
        l_name = request.POST.get('l_name')
        state = request.POST.get('state')
        address = request.POST.get('address')
        place = request.POST.get('place')
        email = request.POST.get('email')
        pin = request.POST.get('pin')
        number = request.POST.get('number')
        total = request.POST.get('total')
        obj = OrderDB(First_Name=f_name,Last_Name=l_name,State=state,Place=place,Email=email,PIN_CODE=pin,
                      Mobile_Number=number,Address=address,TotalPrice=total)
        obj.save()
        messages.success(request, 'Checkout Successful ')
        return redirect(payment)

def payment(request):
    cart_total = 0
    user_name = request.session.get('Name')
    if user_name:
        cart_total = CartDB.objects.filter(UserName=user_name).count

        customer = OrderDB.objects.order_by('-id').first()

        payy = customer.TotalPrice
        amount = int(payy*1000)
        pay_str = str(amount)

        if request.POST == "POST":
            order_currency = 'INR'
            client = razorpay.Client(auth=('rzp_test_0ib0jPwwZ7I1lT', 'VjHNO5zKeKxz8PYe7VnzwxMR'))
            payment = client.order.create({'amount':amount,'currency':order_currency})

    categories = CategoryDB.objects.all()
    return render(request, 'Payment.html',{'cart_total' : cart_total, 'categories' : categories,
                                           'pay_str':pay_str})



def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            # Save the email to database
            subscriber, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Subscribed successfully!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect(request.META.get('HTTP_REFERER', '/'))
