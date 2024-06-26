# Generated by Django 4.2.11 on 2024-04-06 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('idade', models.IntegerField(verbose_name=2)),
                ('chip', models.IntegerField(verbose_name=15)),
                ('info_animais', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porte', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Raca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raca', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='historico_medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_medica', models.CharField(max_length=50)),
                ('voluntario_name', models.EmailField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='especie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.especie'),
        ),
        migrations.AddField(
            model_name='animal',
            name='porte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.porte'),
        ),
        migrations.AddField(
            model_name='animal',
            name='raca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.raca'),
        ),
        migrations.AddField(
            model_name='animal',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_animais.sexo'),
        ),
    ]
