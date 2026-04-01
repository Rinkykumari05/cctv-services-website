from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Inquiry, Product, Package, Testimonial, Gallery

def home(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        property_type = request.POST.get('property_type')
        message = request.POST.get('message')

        Inquiry.objects.create(
            name=name,
            phone=phone,
            property_type=property_type,
            message=message
        )

        send_mail(
            subject='New CCTV Inquiry Received',
            message=f'''
New inquiry received:

Name: {name}
Phone: {phone}
Property Type: {property_type}
Message: {message}
''',
            from_email=None,
            recipient_list=['servizable@gmail.com'],
            fail_silently=False,
        )

        return redirect('/?success=true')

    if request.GET.get('success') == 'true':
        success = True

    products = Product.objects.all()
    packages = Package.objects.all()
    testimonials = Testimonial.objects.all()
    gallery_items = Gallery.objects.all()

    return render(request, 'website/index.html', {
        'success': success,
        'products': products,
        'packages': packages,
        'testimonials': testimonials,
        'gallery_items': gallery_items
    })