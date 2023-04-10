from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('pizza/', views.ListPageView.as_view(), name="pizza_head"),
    path('<int:pk>', views.CategoryPageView.as_view(), name="pizza_category"),
]
