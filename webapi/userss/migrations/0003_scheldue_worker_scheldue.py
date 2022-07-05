# Generated by Django 4.0.3 on 2022-06-26 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0002_client_alter_worker_specialisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scheldue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_working', models.TimeField()),
                ('start_break', models.TimeField(null=True)),
                ('end_break', models.TimeField(null=True)),
                ('end_working', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='worker',
            name='scheldue',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='userss.scheldue'),
        ),
    ]