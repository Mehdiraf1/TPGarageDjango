# Generated by Django 5.0.7 on 2024-07-18 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immatriculation', models.CharField(max_length=100)),
                ('marque', models.CharField(max_length=100)),
                ('modele', models.CharField(max_length=100)),
                ('etat', models.CharField(max_length=100)),
            ],
        ),
    ]