# Generated by Django 5.0.6 on 2024-05-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_remove_lfgalert_currentpartycount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lfgalert',
            name='currentPartyCount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='interest',
            field=models.CharField(choices=[('BG', 'Board Games'), ('VG', 'Video Games'), ('SP', 'Sports'), ('DI', 'Dinner'), ('HO', 'Hang out')], default='BG', max_length=30),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='locationCity',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='locationState',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='locationZip',
            field=models.CharField(default=55555, max_length=7),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='meetupAddress',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='neededPartyCount',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='lfgalert',
            name='partySpecifics',
            field=models.TextField(blank=True),
        ),
    ]
