# Generated by Django 3.2.9 on 2021-11-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzdevumi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='image',
            field=models.ImageField(blank=True, upload_to='visits'),
        ),
    ]