from django.shortcuts import redirect, render, get_object_or_404

from .models import Product, Review


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        
        if content:
            review = Review.objects.create(
                product=product,
                rating=rating,
                content=content,
                created_by=request.user
            )
            return redirect("product:product", slug=slug)
    
    return render(request, 'product/product.html', {'product':product})