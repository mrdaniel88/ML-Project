# Generated by Django 2.1.7 on 2019-12-03 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0004_auto_20191203_0353'),
    ]

    operations = [
        migrations.AddField(
            model_name='simage',
            name='source',
            field=models.CharField(choices=[('1', 'Red Neuronal 1'), ('2', 'Red Neuronal 2'), ('3', 'Naive Bayes 1'), ('4', 'Naive Bayes 2')], default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='simage',
            name='status',
            field=models.CharField(choices=[('0', 'Colombia Geoscience Datacube IDEAM'), ('1', 'United States Geological Survey USGS')], max_length=2),
        ),
    ]