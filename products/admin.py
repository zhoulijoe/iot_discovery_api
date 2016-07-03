from django.contrib import admin

from products.models import Product, Category, Company, TargetMarket


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)


class TargetMarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_categories', 'company')
    list_filter = ('categories',)
    filter_horizontal = ('categories', 'target_markets')
    raw_id_fields = ('company',)

    def get_categories(self, obj):
        return ', '.join([c.name for c in obj.categories.all()])
    get_categories.short_description = 'categories'


admin.site.register(Category, CategoryAdmin)
admin.site.register(TargetMarket, TargetMarketAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Product, ProductAdmin)
