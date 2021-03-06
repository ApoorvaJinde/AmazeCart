# Generated by Django 3.1.4 on 2021-06-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210607_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='area',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='district',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='home_number',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
