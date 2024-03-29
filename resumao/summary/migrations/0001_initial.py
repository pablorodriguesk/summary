# Generated by Django 2.2.2 on 2019-06-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('sexo', models.CharField(choices=[('feminino', 'Feminino'), ('masculino', 'Masculino')], max_length=15)),
                ('formacao', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('area', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('cidade', models.CharField(max_length=20)),
                ('likendin', models.CharField(max_length=20)),
                ('instagram', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
    ]
