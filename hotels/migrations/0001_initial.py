# Generated by Django 5.1.4 on 2024-12-12 08:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("base_user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="HotelRoom",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("room_id", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="base_user.hotel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FeedbackDescription",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("overall_rating", models.PositiveSmallIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "room",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="hotels.hotelroom",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question", models.TextField()),
                ("question_az", models.TextField(null=True)),
                ("question_en", models.TextField(null=True)),
                ("question_tr", models.TextField(null=True)),
                ("question_ru", models.TextField(null=True)),
                ("question_ar", models.TextField(null=True)),
                ("question_ko", models.TextField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="base_user.hotel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.PositiveSmallIntegerField()),
                (
                    "description",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedback_description",
                        to="hotels.feedbackdescription",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feedbacks",
                        to="hotels.question",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("title_az", models.CharField(max_length=250, null=True)),
                ("title_en", models.CharField(max_length=250, null=True)),
                ("title_tr", models.CharField(max_length=250, null=True)),
                ("title_ru", models.CharField(max_length=250, null=True)),
                ("title_ar", models.CharField(max_length=250, null=True)),
                ("title_ko", models.CharField(max_length=250, null=True)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="services_photo/"
                    ),
                ),
                (
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=7),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("description_az", models.TextField(blank=True, null=True)),
                ("description_en", models.TextField(blank=True, null=True)),
                ("description_tr", models.TextField(blank=True, null=True)),
                ("description_ru", models.TextField(blank=True, null=True)),
                ("description_ar", models.TextField(blank=True, null=True)),
                ("description_ko", models.TextField(blank=True, null=True)),
                ("slug", models.SlugField(allow_unicode=True, blank=True, null=True)),
                ("etp", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hotel_services",
                        to="base_user.hotel",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TechnicalService",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("title_az", models.CharField(max_length=250, null=True)),
                ("title_en", models.CharField(max_length=250, null=True)),
                ("title_tr", models.CharField(max_length=250, null=True)),
                ("title_ru", models.CharField(max_length=250, null=True)),
                ("title_ar", models.CharField(max_length=250, null=True)),
                ("title_ko", models.CharField(max_length=250, null=True)),
                (
                    "icon",
                    models.ImageField(
                        blank=True, null=True, upload_to="tech_service_icons"
                    ),
                ),
                ("order_number", models.PositiveSmallIntegerField()),
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="technical_services",
                        to="base_user.hotel",
                    ),
                ),
            ],
        ),
    ]
