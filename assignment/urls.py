
from django.contrib import admin
from django.urls import path,include
from . import views
from accounts.views import account_signup_view,UserEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),

    path("accounts/signup/", view=account_signup_view),

    path('accounts/', include('allauth.urls')), # new
    path('', views.home,name='home'), # new
    path('accounts/',include('accounts.urls')),



]
