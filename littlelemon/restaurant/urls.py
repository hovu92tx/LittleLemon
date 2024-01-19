from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('book', views.book, name="book"),
    path('menu', views.menu, name="menu"),
    path('menu_item/<int:pk>', views.display_menu_item, name="menu_item"),
    path('reservations/', views.reservations, name='reservations'),
    #-----------------------------------------------------------------
    #API URLs
    path('bookings/', views.BookingsView.as_view(), name= 'api_booking_view'),
    path('bookings/<int:pk>', views.SingleBookingView.as_view()),
    path('menu-items/', views.MenuView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('categories/', views.CategoriesView.as_view()),
    path('categories/<int:pk>', views.SingleCategoriesView.as_view()),
    path('ratings', views.RatingsView.as_view()),
    path('cart', views.CartView.as_view()),
    path('orders/', views.OrderView.as_view()),
    path('orders/<int:pk>', views.SingleOrderView.as_view()),
    path('groups/manager/users', views.GroupViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
        {'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('api-token-auth/', obtain_auth_token),
]