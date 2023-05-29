from django.urls import path, include
from . import views
app_name='search_app'

urlpatterns = [
    path('/', views.SearchResult,name='SearchResult'),
    #path('<slug:c_slug>/',views.allProdCat,name='product_by_category'),
    #path('<slug:c_slug>/<slug:product_slug>/', views.proDetails, name='prodCatdetail'),

]
