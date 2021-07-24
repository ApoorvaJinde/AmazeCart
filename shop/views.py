from django.db.models import query
from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User

import math

def show(request):
    return redirect('shop:front')


def prod(request):
    return redirect('shop:product_list')

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def front(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/front.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_front(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list_front.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
def SearchMatch(query,item):
    if query in item.description.lower() or query in item.name.lower() :
        return True
    else:
        return False



def search(request):
    prodt=Product.objects.all()
    allprods=[]
    if request.method=="POST":
        query=request.POST['search']
        prod=Product.objects.filter(name__contains=query,description__contains=query).all()
        #catProds=Product.objects.values('category','id')
        #cats={item['category'] for item in catProds}
        #for cat in cats:
           # prodtemp=Product.objects.filter(category=cat)
            #prod =[item for item in prodtemp if SearchMatch(query,item)]
            #n=len(prod)
            #nSlides=n//4+ math.ceil((n/4)-(n//4))
            #allprods.append([prod,range(1,nSlides),nSlides])
        return render(request,'shop/product/search.html',{'prod':prod,'query':query}
                  )
    else:
        return render(request,'shop/product/search.html',{}
                  )


def searched(request):
 
    if request.method=="POST":
        query=request.POST['search']
        prod=Product.objects.filter(name__icontains=query,description__icontains=query).all()
        
        return render(request,'shop/product/searched.html',{'prod':prod,'query':query}
                  )
    else:
        return render(request,'shop/product/searched.html',{}
                  )

