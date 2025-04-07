from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View


# Create your views here.
def hello(request):
    return HttpResponse('Hello!', status=400, reason="Error!!!")


def simple_post(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        return HttpResponse(f"You said: {message}!!!")
    return render(request, 'simple_post.html')


def index(request):
    title = 'Главная страница'
    text = "Мой текст"
    context = {
        'title': title,
        'text': text
    }
    return render(request, 'index.html', context)


products = [
    {'id': 1, 'name': 'Iphone', 'category': 'smartphone', 'price': 10000},
    {'id': 2, 'name': 'Samsung', 'category': 'smartphone', 'price': 9000},
    {'id': 3, 'name': 'Xiaomi', 'category': 'smartphone', 'price': 7000},
    {'id': 4, 'name': 'Oppo', 'category': 'smartphone', 'price': 6000},
    {'id': 5, 'name': 'Huawei', 'category': 'smartphone', 'price': 6500},
    {'id': 6, 'name': 'Наушники', 'category': 'accessories', 'price': 500},
    {'id': 7, 'name': 'Микрофон', 'category': 'accessories', 'price': 900},
    {'id': 8, 'name': 'Моноблок', 'category': 'computer', 'price': 9000},
    {'id': 9, 'name': 'Компьютер', 'category': 'computer', 'price': 11000},
    {'id': 10, 'name': 'Ноутбук', 'category': 'computer', 'price': 34000},
    {'id': 11, 'name': 'планшет Samsung', 'category': 'планшет', 'price': 14000}
]


def index3(request):
    return render(request, 'index3.html', {'products': products})


def product_list(request):
    category = request.GET.get('category')
    if category:
        filtered_products = [product for product in products if product['category'] == category]
    else:
        filtered_products = products

    return render(request, 'index3.html', {'products': filtered_products})


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        products.append({
            'id': len(products) + 1,
            'name': name,
            'category': category,
            'price': int(price)
        })
        return redirect('index3')
    return render(request, 'add_product.html')


class Post(View):
    def get(self, request):
        return HttpResponse('GET')


class Index2(TemplateView):
    template_name = 'index2.html'


def index4(request):
    text = 1
    name = "Tom"
    list = [1.1, 2.2, 3.3]
    len_list = len(list)
    context = {
        "text": text,
        "name": name,
        'list': list,
        'len_list': len_list
    }
    return render(request, "index4.html", context)
