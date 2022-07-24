# Generated by Django 4.0.5 on 2022-07-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_user_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='paidHint',
            field=models.TextField(default='Extra Hint'),
        ),
        migrations.AddField(
            model_name='user',
            name='currency',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='user',
            name='doublerTaken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='doublerTakenTime',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='paidHintTaken',
            field=models.BooleanField(default=False),
        ),
    ]
