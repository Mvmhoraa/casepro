# Generated by Django 4.0.2 on 2022-10-11 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0009_generate_api_tokens"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="is_email_valid",
            field=models.BooleanField(default=True),
        ),
    ]
