
from product.views import category_show, ProductDetail
from django.urls.conf import path


urlpatterns = [
    path('<slug:category_slug>', category_show, name='category_show'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]