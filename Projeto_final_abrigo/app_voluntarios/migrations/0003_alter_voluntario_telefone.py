# Generated by Django 4.2.11 on 2024-04-07 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_voluntarios', '0002_alter_voluntario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='telefone',
            field=models.IntegerField(max_length=11, verbose_name='Telefone'),
        ),
    ]