from django.urls import path
from . import views
from product import views as product_views  # Correct way to import product app views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('help/', views.help_page_view, name='help'),
    path('basket/', views.basket_page_view, name='basket'),
    path('contents/', views.contents_page_view, name='contents'),
    path('update_item/', product_views.updateItem, name="update_item"),  # Corrected reference
    path('login/', views.login_page_view, name='login'),
    path('register/', views.register_page_view, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('cheapest_price/', views.cheapest_price_view, name='cheapest_price'),
]
