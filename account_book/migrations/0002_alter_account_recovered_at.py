# Generated by Django 4.1.2 on 2022-11-04 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_book", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="recovered_at",
            field=models.DateTimeField(null=True),
        ),
    ]