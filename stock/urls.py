from django.urls import path
from .import views


urlpatterns = [
    path('', views.list_items, name='home'),
    path('items/', views.list_items, name='list_items'),
    path('total_list/', views.total_list, name='total_list'),
    path('add_stock/', views.add_stock_form, name='add_stock'),
    path('add_sup/', views.add_sup_form, name='add_sup'),
    path('add_category/', views.add_catrgory_form, name='add_category'),
    path('update_stock/<str:pk>/', views.Update_stock_form, name="update_stock"),
    path('delete_stock/<str:pk>/', views.delete_stock, name="delete_stock"),
    path('stock_details/<str:pk>/', views.stock_details, name="stock_details"),

    path('logout/', views.logoutuser, name="logout"),

   

    
]

