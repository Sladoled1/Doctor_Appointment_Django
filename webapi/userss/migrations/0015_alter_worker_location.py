# Generated by Django 4.0.3 on 2022-06-30 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0014_alter_worker_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='userss.worklocation'),
        ),
    ]