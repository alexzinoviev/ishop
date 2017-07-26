from django.contrib import admin
from .models import Product, Brand

#@admin.register(Product)
class ProductAdmin(admin.StackedInline):
    #pass
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','desc', 'cost', 'active')
    model = Product

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    inlines = [
        ProductAdmin,
    ]


# Register your models here.

#admin.site.register(Product, ProductAdmin)

