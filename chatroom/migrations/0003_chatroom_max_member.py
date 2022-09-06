# Generated by Django 4.1 on 2022-09-06 02:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chatroom", "0002_rename_id_chatroom_room_id_chatroom_creation_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatroom",
            name="max_member",
            field=models.IntegerField(
                default=50,
                validators=[
                    django.core.validators.MaxValueValidator(100),
                    django.core.validators.MinValueValidator(1),
                ],
            ),
        ),
    ]
