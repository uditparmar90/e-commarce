from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import FeedbackForm
from django.contrib import messages

# Create your views here.


def index(request):
    user = "pouya"
    products_numb = 7
    products = Product.objects.all().order_by('id')[:4]
    # suits=Product.objects.filter(brand__title="Pouya")
    return render(request, "products/home.html",{
        "name":user,
        "product_numb": products_numb,
        "products": products,
    })

def signup(request):
    return render(request, "products/signup.html")

def product_cat(request, product):
    if product =="suits" or product=="dresses" or product=="shirts" or product=="shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("The page you are looking for doesn't exist.")

def product_page(request,product_brand,product_slug):
    product=Product.objects.get(slug=product_slug)

    form=FeedbackForm()
    if request.method=="GET":
        return render(request,"products/product_detail_page.html",{"product":product,"form":form})
    else:
        form=FeedbackForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            messages.success(request,"Thanks for your review!")

        return render(request,"products/product_detail_page.html",{"product":product,"form":form})
        

    
