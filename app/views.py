from app.models import Metric

from django.db.models import Sum
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework import serializers


class MetricSerializer(serializers.ModelSerializer):
    cpi = serializers.ReadOnlyField(required=False)

    class Meta:
        model = Metric
        fields = '__all__'

        # Make all fields not required
        extra_kwargs = {
            field: {'required': False}
            for field in model().get_model_fields()
        }


class MetricFilter(filters.FilterSet):
    date_from = filters.DateFilter(field_name='date', lookup_expr='gt')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lt')

    class Meta:
        model = Metric
        fields = ['channel', 'country', 'os', 'date']


class MetricList(ListAPIView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filter_backends = [OrderingFilter, filters.DjangoFilterBackend]
    filterset_class = MetricFilter
    ordering_fields = '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()

        query_params = self.request.query_params
        if query_params:
            group_by = query_params.get('group_by')
            if group_by:
                queryset = queryset.values(*group_by.split(','))

            sum_of = query_params.get('sum')
            if sum_of:
                # create dict to annotate smth like cpi=Sum('cpi'), impressions=Sum('impressions')
                sum_query = {
                    metric: Sum(metric) for metric in sum_of.split(',')
                }
                queryset = queryset.annotate(**sum_query)

        return queryset
