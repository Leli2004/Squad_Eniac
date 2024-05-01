# Generated by Django 4.2.11 on 2024-04-07 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_voluntarios', '0005_alter_voluntario_info_geral'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voluntario',
            name='status',
        ),
        migrations.AddField(
            model_name='voluntario',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='PedidoInscricao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Pendente'), ('a', 'Aprovado'), ('r', 'Recusado')], default='p', max_length=1)),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_voluntarios.voluntario')),
            ],
        ),
    ]
