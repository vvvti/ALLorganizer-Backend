# Generated by Django 3.1.2 on 2021-01-30 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='completebloodcount',
            name='cbc_time',
            field=models.TimeField(default='12:00:00', verbose_name='Godzina badania'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='pct',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='PCT'),
        ),
        migrations.AlterField(
            model_name='completebloodcount',
            name='cbc_date',
            field=models.DateField(verbose_name='Data badania'),
        ),
    ]
