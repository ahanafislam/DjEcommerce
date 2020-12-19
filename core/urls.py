from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    #Urls for Class Based View
    path("", views.HomeView.as_view(), name="home"),
    path("product/<slug>/", views.ItemDetailView.as_view(), name="product"),
    path("order-summary/", views.OrderSummaryView.as_view(), name="order-summary"),

    #Urls for Function Based View
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path('remove-single-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path("checkout/", views.checkout, name="checkout"),
]