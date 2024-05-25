from django.urls import path,include
from . import views

urlpatterns = [
    path('userlogin/', views.userlogin,name='userlogin'),
    path('userregistration/', views.userregistration,name='userregistration'),
    path('logout/', views.logout, name='logout'),
    path('owner_login/', views.owner_login,name='owner_login'),
    path('owner_registrations/', views.owner_registrations,name='owner_registrations'),
    path('owner_logout/', views.owner_logout, name='owner_logout'),
    path('', views.index,name='index'),
    path('userhome/', views.userhome,name='userhome'),
    path('owner_home/', views.owner_home,name='owner_home'),
    path('contact/', views.contact,name='contact'),
    path('user_cancel/', views.user_cancel,name='user_cancel'),
    path('delete_data/<int:id>/', views.delete_data, name='delete_data'),
     path('user_cancelbooking/', views.user_cancelbooking, name='user_cancelbooking'),
    path('edit_data/<int:id>/', views.edit_data, name='edit_data'),
    path('offgrid_slot/',views.offgrid_slot,name='offgrid_slot'),
    path('hybrid_slot/',views.hybrid_slot,name='hybrid_slot'),
    path('add_hybridslot/',views.add_hybridslot,name='add_hybridslot'),
    path('add_offgridslot/',views.add_offgridslot,name='add_offgridslot'),





    # path('about/', views.about,name='about'),
     path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminregistration/', views.adminregistration, name='adminregistration'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('view_user/',views.view_user, name='view_user'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('add_stations/', views.add_stations, name='add_stations'),
    path('search/',views.search,name='search'),
    path('book_slots/',views.book_slots,name='book_slots'),
    path('payment/',views.payment,name='payment'),
    path('view_slots/',views.view_slots,name='view_slots'),
    path('view_booking/',views.view_booking,name='view_booking'),
    path('user_review/',views.user_review,name='user_review'),
    path('view_paymenthistory/',views.view_paymenthistory,name='view_paymenthistory'),
    ]