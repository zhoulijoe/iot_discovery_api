from django.db import models
from django_countries.fields import CountryField
from model_utils.models import TimeStampedModel

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class TargetMarket(BaseModel):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Company(BaseModel):
    name = models.CharField(max_length=500, unique=True)
    country = CountryField(blank_label='select country', blank=True)
    site = models.URLField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=500)
    company = models.ForeignKey(Company)
    categories = models.ManyToManyField(Category)
    official_link = models.URLField(max_length=200, blank=True)
    selling_point = models.TextField(blank=True)
    target_markets = models.ManyToManyField(TargetMarket, blank=True)
    available = models.BooleanField(default=True)
    has_app = models.BooleanField(default=False)
    launch_date = models.DateField(blank=True, null=True)
    use_case = models.TextField(blank=True)
    tech_note = models.TextField(blank=True)
    description = models.TextField(blank=True)
    main_image = models.ImageField(blank=True)
    main_video = models.URLField(max_length=200, blank=True)
    price_dollar = models.FloatField(blank=True, null=True)
    price_rmb = models.FloatField(blank=True, null=True)
    price_euro = models.FloatField(blank=True, null=True)

    class Meta:
        unique_together = ('name', 'company')
        ordering = ['-created']

    def __str__(self):
        return self.name
