# Generated by Django 4.0 on 2022-08-19 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0079_alter_dataset_description_dataset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset_description',
            name='dataset',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='desc', to='data.dataset'),
        ),
    ]
