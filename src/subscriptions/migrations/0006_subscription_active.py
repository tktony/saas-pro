# Generated by Django 5.0.10 on 2025-02-10 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0005_alter_subscription_permissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]
