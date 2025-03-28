from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="WednySalon API",
      default_version='v1',
      description="For developer to testing",
    #   terms_of_service="https://www.google.com/policies/terms/",    # 條款
    #   contact=openapi.Contact(email="contact@snippets.local"),  # contact email
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)