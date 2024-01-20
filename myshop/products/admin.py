from django.contrib import admin
from .models import Shirt, Product, Brand,Address,Category
# Register your models here.

class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title", "id", "is_bestseller")
    list_filter = ("is_bestseller",)
    search_fields = ("title","category","brand")

admin.site.register(Shirt)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Address)
admin.site.register(Product, productAdmin)