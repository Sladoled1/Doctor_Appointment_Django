# Generated by Django 4.0.3 on 2022-06-26 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0003_scheldue_worker_scheldue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='scheldue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='userss.scheldue'),
        ),
    ]