# Generated by Django 4.2.2 on 2023-08-01 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rutbe_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutbe',
            name='person',
        ),
        migrations.AddField(
            model_name='person',
            name='rutbe',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.rutbe'),
        ),
    ]
