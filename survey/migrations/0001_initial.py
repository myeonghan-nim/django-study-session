# Generated by Django 5.1.3 on 2024-11-18 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SurveyResponse",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.TextField(blank=True, null=True)),
                ("step1_data", models.JSONField(blank=True, null=True)),
                ("step2_data", models.JSONField(blank=True, null=True)),
                ("step3_data", models.JSONField(blank=True, null=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
