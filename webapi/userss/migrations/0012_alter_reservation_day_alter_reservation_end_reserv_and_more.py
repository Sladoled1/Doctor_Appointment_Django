# Generated by Django 4.0.3 on 2022-06-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0011_alter_reservation_client_alter_reservation_docid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='day',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='end_reserv',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='procedure',
            field=models.CharField(choices=[('Consultation', 'Consultation'), ('Operation', 'Operation')], default=('Operation', 'Operation'), max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_reserv',
            field=models.TimeField(null=True),
        ),
    ]
