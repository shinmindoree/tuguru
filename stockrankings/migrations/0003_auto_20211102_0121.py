# Generated by Django 3.2.7 on 2021-11-01 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockrankings', '0002_auto_20211030_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockrankings',
            name='earningdate',
        ),
        migrations.RemoveField(
            model_name='stockrankings',
            name='marketcap',
        ),
        migrations.RemoveField(
            model_name='stockrankings',
            name='revenue',
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='currency',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='industry',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='marketCap',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='netIncomeToCommon',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='priceToBook',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='sector',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='totalRevenue',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stockrankings',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stockrankings',
            name='dividendyield',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockrankings',
            name='grossprofit',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockrankings',
            name='operatingCashflow',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='stockrankings',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
