# Generated by Django 4.2.3 on 2023-07-27 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_person_rutbe'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='sekil',
            field=models.ImageField(blank=True, null=True, upload_to='main/uploads/%d/%m/%Y', verbose_name='Şəkil'),
        ),
    ]