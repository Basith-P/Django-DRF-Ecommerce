from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
]
