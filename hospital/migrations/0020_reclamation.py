# Generated by Django 3.0.5 on 2023-06-17 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_doctor_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
                ('reclamation', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
