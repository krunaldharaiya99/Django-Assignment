# imports
from django import forms
from django.contrib import admin
from products.models import Product
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def save(self, commit=True):
        product = super().save(commit=False)
        if commit:
            product.save()
        return product

class ProductChangeForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
        ]

class ProductAdmin(admin.ModelAdmin):
    # The forms to add and change user instances
    form = ProductChangeForm
    add_form = ProductCreationForm
    
    list_display = ('title', 'content', 'price', 'sale_price')
    list_filter = ('title', "price")

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'content', 'price'),
        }),
    )

    search_fields = ('title', )
    ordering = ('price',)
    filter_horizontal = ()

admin.site.register(Product, ProductAdmin)