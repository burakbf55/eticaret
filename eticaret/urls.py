"""eticaret URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from page.views import index
from django.urls import path,include
from django.conf import settings
from product.views import category_show, ProductDetail


urlpatterns = [
    path('', index, name='index'),
    path('<slug:category_slug>', category_show, name='category_show'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('manage/', include('page.urls')),
    path('cart/', include('cart.urls')),
    path('users/',include('users.urls')),
    path('admin/', admin.site.urls),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)