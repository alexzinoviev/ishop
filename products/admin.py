from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #pass
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name','desc', 'cost', 'active')

# Register your models here.

#admin.site.register(Product, ProductAdmin)

