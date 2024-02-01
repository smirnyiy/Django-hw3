from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from .models import User, Product, Orders

def hello(request):
    return HttpResponse("Hello World from function!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class")

def year_post(request, year):
    text = ""
    return  HttpResponse(f"Post from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        return HttpResponse(f"Post from {month}/{year}<br>{text}")

def post_detail(request, year, month, slug):
    post = {
        "year":year,
        "month":month,
        "slug":slug,
        "title":"Кто быстрее создает списки Python, list(), или []",
        "content":"В процессе написания очередной программы задумался над тем, "
                  "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii': False})

def my_view(request):
    context = {'name': 'John'}
    return render(request, 'myapp/my_templates.html', context)

class TemplIf(TemplateView):
    template_name = 'myapp/templ_if.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Привет, мир!'
        context['number'] = 5
        return context

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'желтый',
        'знать': 'зеленый',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый'
    }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp/templ_for.html', context)

def index(requset):
    return render(requset, 'myapp/index.html')

def about(requset):
    return render(requset, 'myapp/about.html')

def user_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Orders.objects.filter(customer=user).order_by('date_ordered')
    return render(request, 'myapp/user_order.html', {'user': user, 'orders': orders})

def order_full(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    return render(request, 'myapp/order_full.html', {'order': order})