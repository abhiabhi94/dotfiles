Vim�UnDo� �*7����v!0�щ��V�ԭ2�޹1��V��   "                                   a�?    _�                             ����                                                                                                                                                                                                                                                                                                                                                             a��    �         !    5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             a�>     �               "   from django.db import models   $from django.urls import reverse_lazy   6from django.utils.translation import gettext_lazy as _       +from product.managers import ProductManager           class Product(models.Model):   +    name = models.CharField(max_length=100)   6    sku = models.SlugField(unique=True, db_index=True)   $    description = models.TextField()   O    is_active = models.BooleanField(default=False, verbose_name=_('is_active'))   8    created_at = models.DateTimeField(auto_now_add=True)   4    updated_at = models.DateTimeField(auto_now=True)           objects = ProductManager()           class Meta:   "        ordering = ('updated_at',)           def get_absolute_url(self):   =        return reverse_lazy('product:detail', args=[self.pk])           def serialize(self):           return {               'id': self.id,               'name': self.name,               'sku': self.sku,   ,            'description': self.description,   (            'is_active': self.is_active,   0            'url': str(self.get_absolute_url()),   /            'created_at': str(self.created_at),   /            'updated_at': str(self.updated_at),   	        }5��