# Generated by Django 4.0.3 on 2022-06-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0005_remove_client_reservation_alter_scheldue_end_break_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='docid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]