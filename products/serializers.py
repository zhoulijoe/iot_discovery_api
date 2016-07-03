from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from products.models import Product, Category, Company


class AllowCreateRelatedField(serializers.SlugRelatedField):
    def __init__(self, slug_field=None, **kwargs):
        super(AllowCreateRelatedField, self).__init__(slug_field, **kwargs)

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.slug_field + '__exact': data})
        except ObjectDoesNotExist:
            return self.get_queryset().create(**{self.slug_field: data})
        except (TypeError, ValueError):
            self.fail('invalid')


class ProductSerializer(serializers.ModelSerializer):
    company = AllowCreateRelatedField(slug_field='name', queryset=Company.objects.all())
    categories = AllowCreateRelatedField(many=True, slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'company', 'categories', 'official_link', 'selling_point')
