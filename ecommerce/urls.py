from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter

from apps.product.views import CategoryViewSet

router = DefaultRouter()
router.register("category", CategoryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "api/v1/schema/docs/",
    #     SpectacularSwaggerView.as_view(url_name="schema"),
    #     name="docs",
    # ),
    path(
        "api/v1/schema/docs/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="docs",
    ),
]
