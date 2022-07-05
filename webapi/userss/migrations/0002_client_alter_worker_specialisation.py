# Generated by Django 4.0.3 on 2022-06-25 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('reservation', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='worker',
            name='Specialisation',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dentist', 'Dentist'), ('Dermatologist', 'Dermatologist'), ('Ophthalmologist', 'Ophthalmologist'), ('Surgeon', 'Surgeon')], max_length=50),
        ),
    ]