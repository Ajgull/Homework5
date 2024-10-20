import django_filters
from django.db.models import Q, QuerySet

from core import models


class Product(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Price of order')
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    comment = django_filters.CharFilter(
        field_name='reviews__comment', lookup_expr='icontains', label='Comment contains'
    )
    ordered = django_filters.BooleanFilter(method='filter_in_order', label='In order')
    term = django_filters.CharFilter(method='filter_term', label='')

    class Meta:
        model = models.Product
        fields = ['comment', 'ordered', 'term', 'price_range', 'name']

    def filter_in_order(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        if value is None:
            return queryset
        if value:
            return queryset.filter(details__order__isnull=False).distinct()
        return queryset.exclude(details__order__isnull=False).distinct()

    def filter_term(self, queryset: QuerySet, name: str, value: str) -> QuerySet:
        criterias = Q()
        for t in value.split():
            criterias &= Q(name__icontains=t) | Q(reviews__comment__icontains=t)
        return queryset.filter(criterias).distinct()
