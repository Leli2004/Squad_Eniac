# Generated by Django 4.2.11 on 2024-04-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_animais', '0003_historico_medico_file_alter_animal_chip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='disponivel',
            field=models.BooleanField(default=True),
        ),
    ]
