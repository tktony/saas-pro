# Generated by Django 5.0.10 on 2025-02-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0017_usersubscription_stripe_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersubscription",
            name="user_canceled",
            field=models.BooleanField(default=False),
        ),
    ]
