# Generated by Django 4.1.1 on 2022-09-21 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_remove_chats_room_name_delete_room'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chats',
            options={'ordering': ('message_timestamp',)},
        ),
    ]
