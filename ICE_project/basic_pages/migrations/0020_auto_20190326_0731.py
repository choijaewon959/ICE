# Generated by Django 2.1.7 on 2019-03-25 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_pages', '0019_auto_20190326_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='component_creation_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='component_lastUpdate_date',
            field=models.DateTimeField(null=True),
        ),
    ]