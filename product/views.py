from typing import Counter
from page.views import STATUS
from product.models import Category, Product, Comment
from django.shortcuts import get_object_or_404, render
from .forms import CommentForm
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


def category_show(request, category_slug):
    context = dict()
    context['category'] = get_object_or_404(Category, slug=category_slug)

    # Nav:
    #context['categories'] = Category.objects.filter(
    #    status = STATUS
    #).order_by('title')
    context['items'] = Product.objects.filter(
        category=context['category'],
        status = STATUS,
        stock__gte =1,
    )
    return render(request, 'category_show.html', context)




class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def product_detail(slug,category_slug):
        context = dict()
        products = Product.objects.filter(
            slug=slug,
            status = STATUS,
                #stockgte ne işe yarıyor tam olarak bilmiyorum, eğer bir hata çıkarsa buradan olabilir. Sonradan kontrol et.
        )
        category= Category.objects.all()
        context['category'] = get_object_or_404(Category, slug=category_slug)

        context = {
        'category': category,
        'products': products,
        }
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']

        form = CommentForm()
        post = get_object_or_404(Product, slug=slug)
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        return context


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Product.objects.filter(slug = self.kwargs['slug'])[0]
        comments = post.comment_set.all()

        context['post'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            comment = Comment.objects.create(
                name=name, email=email, content= content, post=post
            )
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)