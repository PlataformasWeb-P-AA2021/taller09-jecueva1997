# Generated by Django 3.2.4 on 2021-06-11 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barriociudadela',
            name='parque',
            field=models.IntegerField(choices=[(1, 'numero 1'), (2, 'numero 2'), (3, 'numero 3'), (4, 'numero 4'), (5, 'numero 5'), (6, 'numero 6')]),
        ),
    ]
