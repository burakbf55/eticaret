from django.shortcuts import render
from page.models import Page,Carousel
from django.contrib.admin.views.decorators import staff_member_required
from page.forms import PageModelForm, CarouselModelForm
from django.utils.text import slugify
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from product.models import Product


# Create your views here.


STATUS = "published"



def index(request):
    context = dict()
    context['images'] = Carousel.objects.filter(
        status = STATUS
    ).exclude(cover_image ='')

    products = Product.objects.filter(
        is_home=True,
        status=STATUS,
        )
    context['products'] = products
    #if not request.session.session_key:
    #    request.session.save()
    return render(request, 'index.html', context)

def page_show(request, slug):
    context = dict()
    context['page'] = get_object_or_404(Page, slug=slug)
    return render(request, 'page.html', context)


@staff_member_required
def page_list(request):
    context= dict()
    context['items'] = Page.objects.all().order_by('-pk')
    return render(request,'page_list.html', context)


def page_create(request):
    context = dict()
    context['items'] = Page.objects.all().order_by('-pk')
    context['form'] = PageModelForm()

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.slug = slugify(item.title.replace('ı','i'))
            item.save()
            messages.success(request, 'Birseyler eklendi')
    return render(request,'form.html', context)

def page_update(request, pk):
    context = dict()
    item = Page.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk: {item.pk} Carousel Create Form"
    context['form'] = PageModelForm(instance=item)

    if request.method == 'POST':
        form = PageModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            if item.slug == "":
                item.slug = slugify(item.title.replace('ı','i'))
            item.save()
            messages.success(request,'güncellendi')
            return redirect('page_update', pk)
    return render(request, 'form.html', context)


def page_delete(request, pk):
    item = Page.objects.get(pk=pk)
    item.status = "deleted"
    item.save()
    return redirect('page_list')



def carousel_list(request):
    context = dict()
    context['carousel'] = Carousel.objects.all().order_by('-pk')
    return render(request, 'carousel_list.html', context)


def carousel_create(request):
    context = dict()
    context['title'] = "Carousel Create Form"
    context['form'] = CarouselModelForm()

    if request.method == 'POST':
        print(request.FILES.get('cover_image'))
        form = CarouselModelForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
        messages.success(request, 'Birseyler eklendi ama ne oldu bilemiyorm')
    return render(request, 'form.html', context)




def carousel_update(request,pk):
    context = dict()
    item = Carousel.objects.get(pk=pk)
    context['title'] = f"{item.title} - pk:{item.pk} Carousel Create Form"
    context['form'] = CarouselModelForm(instance=item)

    if request.method == 'POST':
        form = CarouselModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'güncellendi')
            return redirect('carousel_update',pk)
    
    return render(request,'form.html', context)