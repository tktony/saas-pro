# Generated by Django 5.0.10 on 2025-02-17 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "subscriptions",
            "0013_alter_subscription_options_subscription_featured_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscriptionprice",
            options={
                "ordering": ["subscription__order", "order", "featured", "-updated"]
            },
        ),
    ]
