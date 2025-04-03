from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, View


# Create your views here.
def index(request):
    title = 'Главная страница'
    text = "Мой текст"
    context = {
        'title': title,
        'text':text
    }
    return render(request,'index.html',context)


products = [
    {'name':'Iphone','price':10000},
    {'name':'Samsung','price':9000},
    {'name':'Xiaomi','price':7000},
    {'name':'Oppo','price':6000}
]


def index3(request):
    return render(request,'index3.html',{'products':products})


class ProductListView(View):
    def get(self, request):
        product_items = "<br>".join([f'{p["name"]}: {p["price"]} руб.' for p in products])
        return HttpResponse(product_items)


class Index2(TemplateView):
    template_name='index2.html'


def index4(request):
    text = 1
    name = "Tom"
    list = [1.1, 2.2, 3.3]
    len_list = len(list)
    context = {
        "text": text,
        "name": name,
        'list': list,
        'len_list':len_list
    }
    return render(request, "index4.html", context)
