# imports
from django.contrib import admin
from django.urls import path, include

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('account.urls')),
    path('api/products/', include('products.urls')),
]
