# Generated by Django 3.1.2 on 2020-10-19 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CrpAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crp_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data i godzina badania')),
                ('crp_count', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Wynik CRP')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Badanie CRP',
                'verbose_name_plural': 'Badania CRP',
                'ordering': ('-crp_date',),
            },
        ),
        migrations.CreateModel(
            name='UrineAnalisis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urine_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data i godzina badania')),
                ('color', models.CharField(max_length=45, verbose_name='Kolor')),
                ('specific_gravity', models.DecimalField(decimal_places=4, max_digits=5, verbose_name='Ciężar właściwy')),
                ('ph', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='PH')),
                ('gluccose', models.CharField(blank=True, max_length=45, verbose_name='Glukoza')),
                ('ketone_bodies', models.CharField(blank=True, max_length=45, verbose_name='Ketony')),
                ('urobilinogen', models.CharField(blank=True, max_length=45, verbose_name='Urobilinogen')),
                ('bilurbin', models.CharField(blank=True, max_length=45, verbose_name='Bilurbina')),
                ('protein', models.CharField(blank=True, max_length=45, verbose_name='Białko')),
                ('erythrocyte', models.CharField(blank=True, max_length=45, verbose_name='Erytrocyty')),
                ('leucocyte', models.CharField(blank=True, max_length=45, verbose_name='Leukocyty')),
                ('bacterial', models.CharField(blank=True, max_length=45, verbose_name='Bakterie')),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Uwagi')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Badanie Moczu',
                'verbose_name_plural': 'Badania Moczu',
                'ordering': ('-urine_date',),
            },
        ),
        migrations.CreateModel(
            name='CompleteBloodCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbc_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data i godzina badania')),
                ('leucocyte_count', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Liczba leukocytów')),
                ('erythrocyte_count', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Erytrocyty')),
                ('hemoglobin', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Hemoglobina')),
                ('hematocrit', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Hematokryt')),
                ('mcv', models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True, verbose_name='MCV')),
                ('mch', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='MCH')),
                ('mchc', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='MCHC')),
                ('thrombocyte_count', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Płytki krwi')),
                ('rdw_sd', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='RDW-SD')),
                ('rdw_cv', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='RDW-CV')),
                ('pdw', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='PDW')),
                ('mpv', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='MPV')),
                ('p_lcr', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='P-LCR')),
                ('neutrophils', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Neutrofile')),
                ('lymphocytes', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Limfocyty')),
                ('monocytes', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Monocyty')),
                ('eosinophils', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Eozynofile')),
                ('baso', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Bazofile')),
                ('notes', models.CharField(blank=True, max_length=200, verbose_name='Uwagi')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Morfologia krwi',
                'verbose_name_plural': 'Morfologie krwi',
                'ordering': ('-cbc_date',),
            },
        ),
        migrations.CreateModel(
            name='ALT_AST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_ast_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data i godzina badania')),
                ('alt', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='ALT')),
                ('ast', models.DecimalField(decimal_places=0, max_digits=4, verbose_name='AST')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Badanie ALT, AST',
                'verbose_name_plural': 'Badania ALT, AST',
                'ordering': ('-alt_ast_date',),
            },
        ),
    ]
