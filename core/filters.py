import django_filters
import core.models
from django.db.models import Q


class Product(django_filters.FilterSet):
    # price_range = django_filters.RangeFilter(field_name='price', label='Price of order')
    # name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    comment = django_filters.CharFilter(field_name='reviews__comment', lookup_expr='icontains',
                                        label='Comment contains')
    ordered = django_filters.BooleanFilter(method='InOrder', label='In order')
    term = django_filters.CharFilter(method='Contains_in', label='')

    class Meta:
        model = core.models.Product
        fields = ['comment', 'ordered', 'term']

    def InOrder(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(details__order__isnull=False).distinct()
        return queryset.exclude(details__order__isnull=False).distinct()

    def Contains_in(self, queryset, name, value):
        criterias = Q()
        for t in value.split():
            criterias &= Q(name__icontains=t) | Q(reviews__comment__icontains=t)
        return queryset.filter(criterias).distinct()
