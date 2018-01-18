# Generated by Django 2.0.1 on 2018-01-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contrato', '0003_edital_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vinculo',
            name='valor_carga_horaria',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor por hora'),
        ),
        migrations.AlterField(
            model_name='vinculo',
            name='valor_total_empenho',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor total do empenho'),
        ),
    ]
