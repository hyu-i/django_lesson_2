# Generated by Django 2.2.6 on 2019-11-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='comment',
            field=models.TextField(blank=True, max_length=255, verbose_name='コメント'),
        ),
    ]
