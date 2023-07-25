from django.contrib import admin
from django.urls import path
from CatApp import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Cat API",
      default_version='v1',
      description="This Api is for a catshop. The CatApp database have fields : name, price, breed, description. CatApp has a serializer that convert the data to json. We can run crud operations through view app.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Cat@CatApp.local"),
      license=openapi.License(name="Standard License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # urls for Cat
    path('cats/', views.CatList.as_view(), name='cat-list'),
    path('cats/<int:pk>/', views.CatDetail.as_view(), name='cat-detail'),
    
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]