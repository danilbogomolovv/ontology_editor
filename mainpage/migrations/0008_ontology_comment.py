# Generated by Django 3.1.7 on 2021-05-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0007_auto_20210430_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='ontology',
            name='comment',
            field=models.CharField(default='', max_length=1200),
        ),
    ]
