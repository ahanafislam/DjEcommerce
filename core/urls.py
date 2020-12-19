from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.HomeView.as_view(), name="home"),
    path("product/<slug>/", views.ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    path("checkout/", views.checkout, name="checkout"),
]