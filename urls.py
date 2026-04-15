from django.urls import path
from apps import views

urlpatterns = [
    path('country/', views.country_list, name='country-list'),
    path('city/', views.city_list, name='city-list'),
    path('category/', views.category_list, name='category-list'),
    path('medicine/', views.medicine_list, name='medicine-list'),
    path('medicine/<int:pk>/', views.medicine_detail, name='medicine-detail'),
    path('supplier/', views.supplier_list, name='supplier-list'),
    path('order/', views.order_list, name='order-list'),
    path('order/<int:pk>/status/', views.order_status_update, name='order-status-update'),
]
