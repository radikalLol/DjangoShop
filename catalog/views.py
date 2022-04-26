from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Product, Brand, Category

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_products=Product.objects.all().count()
    num_brands=Brand.objects.count()  # Метод 'all()' применён по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_products':num_products,'num_brands':num_brands},
    )

                   
def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'catalog/templates/product_detail.html',
                  {'product': product})
                  
                  
from django.views import generic

class ProductListView(generic.ListView):
    model = Product
    
class ProductDetailView(generic.DetailView):
    model = Product
    def get_object(self, queryset=None):
        return Product.objects.get(id=self.kwargs.get("id"))
    
class BrandListView(generic.ListView):
    model = Brand
    
class BrandDetailView(generic.DetailView):
    model = Brand
    
    
from cart.form import CartAddProductForm


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/product_detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
    
    

    
