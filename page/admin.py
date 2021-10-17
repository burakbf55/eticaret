from django.contrib import admin
from page.models import Page,Carousel
# Register your models here.

class Pageadmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('title',)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'updated_at',
    )
    list_filter=('status',)
    list_editable=(
        'status',
        'title',
    )

class CarouselAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
    )
    list_filter=('status',)
    
admin.site.register(Page,Pageadmin)
admin.site.register(Carousel,CarouselAdmin)