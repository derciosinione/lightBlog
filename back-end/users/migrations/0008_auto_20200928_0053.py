# Generated by Django 2.2.4 on 2020-09-27 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200928_0050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followersrelation',
            old_name='timestamp',
            new_name='dateCreated',
        ),
    ]