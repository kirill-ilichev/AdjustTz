from django.urls import path

from app.views import MetricList

urlpatterns = [
    path('api/metrics/', MetricList.as_view())
]
