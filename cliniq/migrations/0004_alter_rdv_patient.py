# Generated by Django 4.0.5 on 2022-07-14 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliniq', '0003_alter_rdv_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rdv',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_rdv', to='cliniq.patient'),
        ),
    ]
