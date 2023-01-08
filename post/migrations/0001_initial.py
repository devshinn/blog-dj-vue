# Generated by Django 4.1.5 on 2023-01-07 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="simple on-line text.",
                        max_length=100,
                        verbose_name="DESCRIPTION",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=50, verbose_name="TITLE")),
                (
                    "description",
                    models.CharField(
                        blank=True,
                        help_text="simple on-line text.",
                        max_length=100,
                        verbose_name="DESCRIPTION",
                    ),
                ),
                ("content", models.TextField(verbose_name="CONTENT")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="post/%Y/%m/",
                        verbose_name="IMAGE",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "like",
                    models.PositiveSmallIntegerField(default=0, verbose_name="LIKE"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="post.category",
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="post.tag")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField(verbose_name="CONTENT")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="post/%Y-%m/",
                        verbose_name="IMAGE",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.post",
                    ),
                ),
            ],
        ),
    ]
