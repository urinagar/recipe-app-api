# Generated by Django 3.2.16 on 2022-10-24 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blabla',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
