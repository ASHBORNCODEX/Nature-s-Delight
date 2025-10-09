from django.urls import path
from WebApp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('all_products/', views.all_products, name="all_products"),
    path('single_product/<int:product_id>/', views.single_product, name="single_product"),
    path('filtered_product/<str:ctg_name>/', views.filtered_product, name="filtered_product"),

    path('about_us/', views.about_us, name="about_us"),
    path('contact_us/', views.contact_us, name="contact_us"),
    path('save_contact_page/', views.save_contact_page, name="save_contact_page"),

    path('user_registration/', views.user_registration, name="user_registration"),
    path('save_user_reg/', views.save_user_reg, name="save_user_reg"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),

    path('cart_page/', views.cart_page, name="cart_page"),
    path('save_to_cart/', views.save_to_cart, name="save_to_cart"),
    path('update_cart_item/<int:Item_ID>/', views.update_cart_item, name="update_cart_item"),
    path('cart_item_delete/<int:Item_ID>/', views.cart_item_delete, name="cart_item_delete"),
    path('checkout/', views.checkout, name="checkout"),
    path('save_checkout/', views.save_checkout, name="save_checkout"),
    path('payment/', views.payment, name="payment"),

    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),

]
