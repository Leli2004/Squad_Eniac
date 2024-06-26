# Generated by Django 4.2.11 on 2024-04-08 22:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_voluntarios', '0009_alter_voluntario_telefone'),
        ('app_animais', '0005_alter_animal_chip'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('quant_animais', models.CharField(max_length=500)),
                ('info_geral', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'adotante',
                'verbose_name_plural': 'adotantes',
            },
        ),
        migrations.CreateModel(
            name='Adocao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Pendente'), ('a', 'Aprovado'), ('r', 'Recusado')], default='p', max_length=1)),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('adotante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido', to='app_adotantes.form_user', verbose_name='adotante')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.animal')),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_voluntarios.voluntario')),
            ],
            options={
                'verbose_name': 'Pedido de adoção',
                'verbose_name_plural': 'Pedidos de adoção',
                'ordering': ('-pk',),
            },
        ),
    ]
