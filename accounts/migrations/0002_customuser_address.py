# Generated by Django 3.0.6 on 2021-08-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Address line 1'),
        ),
    ]