# Generated by Django 3.0.5 on 2023-06-17 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_reclamation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamation',
            name='date',
        ),
    ]
