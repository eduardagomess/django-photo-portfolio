from django.urls import path
from portfolios import views

urlpatterns = [
    path("", views.portfolio_index, name="portfolio_index"),
    path("<int:pk>/", views.portfolio_detail, name="portfolio_detail"),
]