# Generated by Django 2.2 on 2020-03-22 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_capacity', models.IntegerField()),
                ('safe_capacity', models.IntegerField()),
                ('service_datetime', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bus_Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
                ('passengers', models.IntegerField()),
                ('id_bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Bus')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=5)),
                ('age', models.IntegerField()),
                ('preconditions', models.BooleanField()),
                ('contact_infected', models.BooleanField()),
                ('ocupation', models.CharField(max_length=50)),
                ('destination_activities', models.CharField(max_length=50)),
                ('home_address', models.CharField(max_length=50)),
                ('destination_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('headway', models.DecimalField(decimal_places=1, max_digits=4)),
                ('date', models.DateField()),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_bus_segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Bus_Segment')),
                ('id_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=20)),
                ('id_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('end_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_end', to='covit.Stop')),
                ('id_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Route')),
                ('initial_stop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stop_initial', to='covit.Stop')),
            ],
        ),
        migrations.AddField(
            model_name='bus_segment',
            name='id_segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Segment'),
        ),
        migrations.AddField(
            model_name='bus',
            name='id_route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covit.Route'),
        ),
    ]
