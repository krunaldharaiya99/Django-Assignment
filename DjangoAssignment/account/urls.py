# imports
from django.urls import path
from account.views import user_login_view, user_registration_view,user_profile_view

# urls
urlpatterns = [
    path('login/', user_login_view),
    path('register/', user_registration_view),
    path('profile/', user_profile_view),
]