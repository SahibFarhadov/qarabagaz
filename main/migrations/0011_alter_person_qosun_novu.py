# Generated by Django 4.2.2 on 2023-08-01 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_rutbe_person_person_rutbe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='qosun_novu',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.qosunnovu'),
        ),
    ]