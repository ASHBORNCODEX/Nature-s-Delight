from django.urls import path
from Admin_App import views

urlpatterns = [
    path('Dashboard/', views.Dashboard,name="Dashboard"),
    path('add_categories/' , views.add_categories,name="add_categories"),
    path('save_category/' , views.save_category,name="save_category"),
    path('view_category/' , views.view_category,name="view_category"),
    path('edit_category/<int:Category_ID>/' , views.edit_category,name="edit_category"),
    path('update_category/<int:Category_ID>/' , views.update_category,name="update_category"),
    path('delete_category/<int:C_ID>/' , views.delete_category,name="delete_category"),

    path('add_product/' , views.add_product,name="add_product"),
    path('save_product/' , views.save_product,name="save_product"),
    path('view_product/' , views.view_product,name="view_product"),
    path('edit_product/<int:Product_ID>/' , views.edit_product,name="edit_product"),
    path('update_product/<int:Product_ID>/', views.update_product, name="update_product"),
    path('delete_product/<int:P_ID>/', views.delete_product, name="delete_product"),

    path('admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('admin_login/', views.admin_login, name="admin_login"),

    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('delete_contact/<int:Contact_ID>/', views.delete_contact, name="delete_contact"),

]