# Generated by Django 4.2.2 on 2023-08-03 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_person_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cinsiyeti',
            field=models.CharField(default='Kişi', max_length=5, verbose_name='Cinsiyyəti seçin'),
        ),
    ]
