# Generated by Django 4.0.6 on 2023-07-23 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCodeCollections', '0003_datastructures_extension'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datastructures',
            name='extension',
        ),
        migrations.AddField(
            model_name='programminglanguages',
            name='extension',
            field=models.CharField(default=None, max_length=10, null=True),
        ),
    ]
