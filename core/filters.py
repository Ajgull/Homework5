import django_filters
import core.models


class Product(django_filters.FilterSet):
    price_range = django_filters.RangeFilter(field_name='price', label='Price of order')
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    comment = django_filters.CharFilter(field_name='reviews__comment', lookup_expr='icontains',
                                        label='Comment contains')
    ordered = django_filters.BooleanFilter(method='InOrder', label='In order')

    class Meta:
        model = core.models.Product
        fields = ['name', 'price_range', 'comment', 'ordered']

    def InOrder(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(details__order__isnull=False).distinct()
        return queryset.exclude(details__order__isnull=False).distinct()
