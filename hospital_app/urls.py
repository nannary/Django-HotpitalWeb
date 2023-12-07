from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('add_drug',views.add_drug),
    path('add_type',views.add_type),
    path('manage_drug',views.manage_drug),
    path('manage_type',views.manage_type),
    path('delete/<int:pk>',views.delete_drug),
    path('deletet/<int:pk>',views.delete_type),
    path('edit/<int:pk>',views.edit_drug),#หน้าแก้ไขข้อมูลยา
    path('editt/<int:pk>',views.edit_type),#หน้าแก้ไขข้อมูลประเภทยา
    path('increase_drug/<int:pk>',views.increase_drug),#หน้าเพิ่มจำนวนยา
    path('decrease_drug/<int:pk>',views.decrease_drug),#หน้าลดจำนวนยา
    path('login',views.custom_login),
    path('logout',views.logout_view),
]