# Generated by Django 4.2.1 on 2023-06-14 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_alter_contactus_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 17, 48, 16, 755963)),
        ),
        migrations.AlterField(
            model_name='replycontact',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 17, 48, 16, 756960)),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 17, 48, 16, 757957)),
        ),
    ]
