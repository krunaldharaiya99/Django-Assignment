# importing Other things
from django.urls import path

# importing views
from products.views import *

# URLs
urlpatterns = [
    path('', product_list_create_view), # Product Create View 
    path('<int:pk>/', product_detail_view), # called a function which redirect to class based API View.
    path('<int:pk>/update/', product_update_view), # called a function which redirect to class based API View.
    path('<int:pk>/delete/', product_destroy_view), # called a function which redirect to class based API View.
]