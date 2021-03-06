# Generated by Django 3.0.8 on 2020-07-25 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calciatore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('ruolo', models.CharField(choices=[('P', 'portiere'), ('D', 'difensore'), ('C', 'centrocampista'), ('A', 'attaccante')], max_length=1)),
                ('squadra', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'calciatore',
                'verbose_name_plural': 'calciatori',
            },
        ),
    ]
