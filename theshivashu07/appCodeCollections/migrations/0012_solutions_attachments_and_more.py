# Generated by Django 4.0.6 on 2023-08-03 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCodeCollections', '0011_problems_subproblem'),
    ]

    operations = [
        migrations.AddField(
            model_name='solutions',
            name='attachments',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='solutionsattachments',
            name='note',
            field=models.CharField(default=None, max_length=1000, null=True),
        ),
    ]
