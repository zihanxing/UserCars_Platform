# Generated by Django 3.0.3 on 2021-06-01 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goodsrecord',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='车龄'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='brand',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='品牌'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='fuel',
            field=models.FloatField(blank=True, null=True, verbose_name='汽油'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='gearbox',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='变速箱'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='horsepower',
            field=models.IntegerField(blank=True, null=True, verbose_name='扭矩'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='image',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='图片'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='mileage',
            field=models.FloatField(blank=True, null=True, verbose_name='公里数'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='model',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='车系'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='torque',
            field=models.IntegerField(blank=True, null=True, verbose_name='马力'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='transfer_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='转手次数'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='volume',
            field=models.FloatField(blank=True, null=True, verbose_name='排量'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='year',
            field=models.IntegerField(blank=True, null=True, verbose_name='年份'),
        ),
        migrations.AlterField(
            model_name='goodsrecord',
            name='name',
            field=models.CharField(max_length=128, verbose_name='汽车名称'),
        ),
    ]