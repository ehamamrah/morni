# Generated by Django 5.0.1 on 2024-01-29 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='provider',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=180, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='providerservice',
            unique_together={('provider', 'service')},
        ),
    ]