# Generated by Django 3.1.1 on 2020-11-19 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0013_underpersonnalitylevel_underskilllevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='underpersonnality_level',
            field=models.ManyToManyField(related_name='precisely_caracterised_by', through='collaborator.UnderPersonnalityLevel', to='collaborator.UnderPersonnality'),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='underskill_level',
            field=models.ManyToManyField(related_name='precisely_can', through='collaborator.UnderSkillLevel', to='collaborator.UnderSkill'),
        ),
        migrations.AlterField(
            model_name='underskilllevel',
            name='underskill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='collaborator.underskill'),
        ),
    ]
