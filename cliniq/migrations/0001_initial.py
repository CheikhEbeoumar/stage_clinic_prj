# Generated by Django 4.0.5 on 2022-07-08 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gérent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prénom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prénom', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
                ('Tél', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Spécialité',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Spécialiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prénom', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=40)),
                ('password', models.CharField(max_length=100)),
                ('nbr_max_rdv', models.IntegerField()),
                ('spécialité', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliniq.spécialité')),
            ],
        ),
        migrations.CreateModel(
            name='RDV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('temp', models.TimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliniq.patient')),
                ('spécialiste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliniq.spécialiste')),
            ],
        ),
    ]