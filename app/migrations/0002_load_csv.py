import csv

from django.db import migrations


def import_csv(apps, _):
    Metric = apps.get_model('app', 'Metric')
    with open('dataset.csv') as f:
        reader = csv.DictReader(f)
        metrics = [Metric(**row) for row in reader]
        Metric.objects.bulk_create(metrics)


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(import_csv, reverse_code=migrations.RunPython.noop)
    ]
