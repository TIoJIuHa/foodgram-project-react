# Generated by Django 4.1.7 on 2023-03-31 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("users", "0003_alter_user_username")]

    operations = [
        migrations.AlterModelOptions(name="follow", options={"ordering": ["-id"]}),
        migrations.AlterModelOptions(name="user", options={"ordering": ["-id"]}),
    ]
