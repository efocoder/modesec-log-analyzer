import django_filters

from analysis.models import Analysis


class Filter(django_filters.FilterSet):
    class Meta:
        model = Analysis
        fields = ['title', 'log_id', 'section']
