# Generated by Django 2.2.7 on 2019-11-05 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_auto_20191105_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberlist',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='number_lists', to='evaluation.Test3'),
        ),
    ]
