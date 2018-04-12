from django.conf import settings
from django_mako_plus import view_function, jscontext
from catalog import models as cmod


@view_function
def process_request(request):
    productList = cmod.Product.objects.filter(status='A')
    context = {
    'productList' : productList,
    }
    return request.dmp.render('products.html', context)
