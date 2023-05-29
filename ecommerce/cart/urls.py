from django.urls import path, include
from . import views
app_name='cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart,name='add_cart'),
    path('', views.cart_details,name='cart_details'),
    path('delete/<int:product_id>/', views.cart_remove,name='cart_remove'),
    path('delete_item/<int:product_id>/', views.cart_delete,name='cart_delete'),
    #path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    #path('<slug:c_slug>/<slug:product_slug>/', views.proDetails, name='prodCatdetail'),

]
