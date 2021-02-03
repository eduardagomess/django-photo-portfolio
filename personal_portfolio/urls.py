from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolios.urls")),
    path("portfolios/", include("portfolios.urls")),
    path("blog/", include("blog.urls")),
]

