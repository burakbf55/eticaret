from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from page.models import DEFAULT_STATUS, STATUS

# Create your models here.
GENDER_CHOICE = [
            ('men','Erkek'),
            ('women','Kadin'),
            ('unisex','UnİSex'),

]

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default=""
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    gender = models.CharField(
        max_length=6,
        default="unisex",
        choices=GENDER_CHOICE,
    )
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{1000 + self.pk} - {self.gender} - {self.title}"


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
    )
    buyer = models.ManyToManyField(User, blank=True)
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to = 'page',
        null = True,
        blank = True,
    )
    price = models.FloatField()
    stock = models.PositiveSmallIntegerField(default=0)
    is_home = models.BooleanField(default=False)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    # order_field = models.SmallIntegerField(default=0)
    createt_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=150)
    content = models.TextField()
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)