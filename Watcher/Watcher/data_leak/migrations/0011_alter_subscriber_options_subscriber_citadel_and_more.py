# Generated by Django 5.0.9 on 2024-11-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_leak', '0010_auto_20210517_0956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscriber',
            options={'verbose_name_plural': 'subscribers'},
        ),
        migrations.AddField(
            model_name='subscriber',
            name='citadel',
            field=models.BooleanField(default=False, verbose_name='Citadel'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='email',
            field=models.BooleanField(default=False, verbose_name='E-mail'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='slack',
            field=models.BooleanField(default=False, verbose_name='Slack'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='thehive',
            field=models.BooleanField(default=False, verbose_name='TheHive'),
        ),
    ]
