# Generated by Django 2.2.6 on 2019-11-04 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='使用地域')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.CharField(max_length=100, verbose_name='開始時期')),
                ('end_time', models.CharField(max_length=100, verbose_name='終了時期')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30, verbose_name='車番')),
                ('chassis_number', models.CharField(max_length=30, verbose_name='車台番号')),
                ('start_use', models.CharField(blank=True, max_length=40, verbose_name='使用開始')),
                ('insurance_number', models.CharField(max_length=50, verbose_name='保険証番号')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cars.Area', verbose_name='地域')),
                ('insurance_period', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='insurance_1', to='cars.Insurance', verbose_name='保険開始時期')),
            ],
        ),
    ]
