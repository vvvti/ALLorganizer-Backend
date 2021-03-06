# Generated by Django 3.1.2 on 2021-02-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0003_auto_20210130_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='completebloodcount',
            name='baso_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Bazofile procentowo'),
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='eosinophils_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Eozynofile procentowo'),
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='lymphocytes_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Limfocyty procentowo'),
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='monocytes_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Monocyty procentowo'),
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='neutrophils_percent',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3, verbose_name='Neutrofile procentowo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='nrbc',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='NRBC'),
        ),
        migrations.AddField(
            model_name='completebloodcount',
            name='nrbc_percent',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='NRBC procentowo'),
        ),
    ]
