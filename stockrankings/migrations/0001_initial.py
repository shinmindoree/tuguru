# Generated by Django 3.2.7 on 2021-10-30 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stockrankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(blank=True, max_length=100)),
                ('ticker', models.CharField(blank=True, max_length=100)),
                ('marketcap', models.IntegerField(blank=True)),
                ('revenue', models.IntegerField(blank=True)),
                ('grossprofit', models.IntegerField(blank=True)),
                ('operatingCashflow', models.IntegerField(blank=True)),
                ('netprofit', models.IntegerField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('employee', models.IntegerField(blank=True)),
                ('dividendyield', models.IntegerField(blank=True)),
                ('earningdate', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tenbaggers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]