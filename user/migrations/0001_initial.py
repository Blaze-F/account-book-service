# Generated by Django 4.1.2 on 2022-11-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "user",
            },
        ),
    ]
