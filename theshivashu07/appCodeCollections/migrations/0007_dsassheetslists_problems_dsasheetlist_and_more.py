# Generated by Django 4.0.6 on 2023-08-03 12:25

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCodeCollections', '0006_problems_solutionscount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DSAsSheetsLists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('reference', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='problems',
            name='dsasheetlist',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='problems_dsasheetlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dsasheetlist_id', models.IntegerField(default=None, null=True)),
                ('problem_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appCodeCollections.problems')),
            ],
        ),
    ]
