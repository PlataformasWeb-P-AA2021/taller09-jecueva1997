# Generated by Django 3.2.4 on 2021-06-11 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordenamiento', '0002_alter_barriociudadela_parque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barriociudadela',
            old_name='numero_edificios',
            new_name='numero_edificio',
        ),
        migrations.AlterField(
            model_name='barriociudadela',
            name='parque',
            field=models.IntegerField(choices=[(1, '1 Parque'), (2, '2 Parques'), (3, '3 Parques'), (4, '4 Parques'), (5, '5 Parques'), (6, '6 Parques')]),
        ),
    ]