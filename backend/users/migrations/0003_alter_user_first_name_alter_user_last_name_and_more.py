# Generated by Django 4.1.7 on 2023-04-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0002_alter_follow_options_alter_user_options_and_more")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=128, verbose_name="password"),
        ),
    ]
