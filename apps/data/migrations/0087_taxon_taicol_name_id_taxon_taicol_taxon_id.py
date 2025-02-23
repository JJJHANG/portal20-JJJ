# Generated by Django 4.0 on 2023-04-10 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0086_taxon_backbone'),
    ]

    operations = [
        migrations.AddField(
            model_name='taxon',
            name='taicol_name_id',
            field=models.IntegerField(default=0, null=True, verbose_name='taicol name id'),
        ),
        migrations.AddField(
            model_name='taxon',
            name='taicol_taxon_id',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='taicol taxon id'),
        ),
    ]
