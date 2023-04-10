from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView, View, ListView, DetailView
from .models import Pizza, Toppings
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class ListPageView(ListView):
    model = Pizza
    context_object_name = "pizza"
    template_name = "list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Pizza/List" 
        return context
    

class CategoryPageView(DetailView):
    def get(self, request, pk):
        pizza = Pizza.objects.get(id=pk)
        topping = pizza.pizza.all()
        context = {
            'title': 'CategoryList',
            'toppings': topping,
        }
        return render(request,'category_list.html', context)

    
    