import django_filters
from .models import *


class Agent_filter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {'username': ['exact']}





