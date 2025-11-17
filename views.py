from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from .models import Product
from .forms import ProductForm
from django.http import FileResponse, Http404
import os
from django.conf import settings
from django.contrib.auth import authenticate

#home view
def home_view(request):
    return render(request, 'Book_app/home.html')

#create view
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Product_list')
    else:
        form = ProductForm()
    return render(request, 'Book_app/product_form.html', {'form': form})

#Read view 
def product_list__view(request):
    products = Product.objects.all()
    return render(request,'Book_app/product_list.html',{'products':products}) 

#upload view
def product_upload (request):
    if request.method == "POST":
        name = request.POST['name']
        file = request.FILES.get('file')
        Product.objects.create(name=name, file=file)
        return redirect('Product_list')
    return render(request, 'Book_app/upload.html')

#download view
def download_file(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if not product.file:
        raise Http404("No file associated with this book.")

    file_path = product.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))

    
#delete view
def product_delete_view(request,product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('Product_list')
    return render (request,'Book_app/product_confirm_delete.html',{'product':product})

#password for deleting
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        password = request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)

        if user is not None:  # password correct
            product.delete()
            return redirect('Product_list')
        else:
            return render(request, 'Book_app/product_confirm_delete.html', {
                'product': product,
                'error': 'Invalid password! Please try again.'
            })

    return render(request, 'Book_app/product_confirm_delete.html', {'product': product})
