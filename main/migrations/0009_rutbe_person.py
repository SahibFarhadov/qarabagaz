# Generated by Django 4.2.2 on 2023-08-01 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_medallar_alter_person_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutbe',
            name='person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.person'),
        ),
    ]
