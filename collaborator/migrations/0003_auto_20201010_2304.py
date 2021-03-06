# Generated by Django 3.1.1 on 2020-10-10 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collaborator.company'),
        ),
        migrations.AddField(
            model_name='project',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='collaborator.company'),
        ),
    ]
