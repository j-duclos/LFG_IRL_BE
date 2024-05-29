# Generated by Django 5.0.6 on 2024-05-19 18:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('BG', 'Board Games'), ('VG', 'Video Games'), ('SP', 'Sports'), ('DI', 'Dinner'), ('HO', 'Hang out')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('XB', 'Xbox'), ('PS', 'PS'), ('PC', 'PC'), ('NT', 'Nintendo'), ('OT', 'Other'), ('NO', 'None')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free', models.CharField(choices=[('WE', 'Weekends'), ('WD', 'Weekdays'), ('WN', 'Weeknights'), ('DA', 'Days'), ('NI', 'Nights'), ('AT', 'Anytime')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('gamer_tag', models.CharField(max_length=50)),
                ('display_gamer_tag', models.BooleanField(default=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField()),
                ('bio', models.TextField()),
                ('radius', models.IntegerField(choices=[(5, '5 miles'), (10, '10 miles'), (20, '20 miles'), (40, '40 miles'), (75, '75 miles'), (100, '100 miles')], default=20)),
                ('coin_balance', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('interest', models.ManyToManyField(related_name='profiles', to='API.interest')),
                ('platform', models.ManyToManyField(related_name='profiles', to='API.platform')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('schedule', models.ManyToManyField(related_name='profiles', to='API.schedule')),
            ],
        ),
    ]
