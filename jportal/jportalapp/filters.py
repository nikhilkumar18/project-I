import django_filters
from .models import jobs

class jobsfilter(django_filters.FilterSet):
    #job  = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = jobs 
        fields = ['job','salary','location']
 