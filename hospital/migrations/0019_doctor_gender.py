# Generated by Django 3.0.5 on 2023-06-16 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
