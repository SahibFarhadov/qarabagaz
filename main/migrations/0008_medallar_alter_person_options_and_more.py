# Generated by Django 4.2.2 on 2023-08-01 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_qosunnovu_rutbe_ad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medallar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=100, null=True, verbose_name='Medal adı')),
                ('sekil', models.ImageField(blank=True, null=True, upload_to='main/uploads/medallar', verbose_name='Şəkil')),
            ],
            options={
                'verbose_name': 'Medal',
                'verbose_name_plural': 'Medallar',
            },
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Şəhid', 'verbose_name_plural': 'Şəhidlər'},
        ),
        migrations.AlterModelOptions(
            name='qosunnovu',
            options={'verbose_name': 'Qoşun növü', 'verbose_name_plural': 'Qoşun növləri'},
        ),
        migrations.AlterModelOptions(
            name='rutbe',
            options={'verbose_name': 'Rütbə', 'verbose_name_plural': 'Rütbələr'},
        ),
        migrations.AddField(
            model_name='qosunnovu',
            name='sekil',
            field=models.ImageField(blank=True, null=True, upload_to='main/uploads/qosun_novleri', verbose_name='Şəkil'),
        ),
        migrations.AddField(
            model_name='rutbe',
            name='sekil',
            field=models.ImageField(blank=True, null=True, upload_to='main/uploads/rutbeler', verbose_name='Şəkil'),
        ),
    ]
