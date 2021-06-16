from django.db import models
from django.db.models import ExpressionWrapper, F, FloatField


class MetricManager(models.Manager):
    def get_queryset(self):
        """Annotates `cpi = spend / installs` in every queryset"""

        return super().get_queryset().annotate(
            cpi=ExpressionWrapper(F('spend') / F('installs'), output_field=FloatField())
        )


class Metric(models.Model):
    date = models.DateField()

    channel = models.CharField(max_length=64)
    country = models.CharField(max_length=2)
    os = models.CharField(max_length=8)

    impressions = models.PositiveSmallIntegerField()
    clicks = models.PositiveSmallIntegerField()
    installs = models.PositiveSmallIntegerField()

    spend = models.FloatField()
    revenue = models.FloatField()

    objects = MetricManager()

    def get_model_fields(self):
        """Get list of fields names."""

        return [field.name for field in self._meta.fields]
