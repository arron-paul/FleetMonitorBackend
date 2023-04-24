from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings

schema_view = get_schema_view(
   openapi.Info(
      title=settings.PROJECT_NAME,
      default_version=settings.PROJECT_VERSION,
      description=settings.PROJECT_DESCRIPTION
   ),
   public=True,
   permission_classes=[
      permissions.AllowAny
   ]
)
