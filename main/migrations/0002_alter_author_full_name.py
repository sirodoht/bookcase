# Generated by Django 5.1.1 on 2024-09-28 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(max_length=200, verbose_name='author full name'),
        ),
    ]
