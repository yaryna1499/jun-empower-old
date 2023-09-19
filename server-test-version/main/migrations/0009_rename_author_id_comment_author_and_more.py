# Generated by Django 4.2.4 on 2023-09-12 19:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0008_alter_specialization_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="comment",
            old_name="author_id",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="customuser",
            old_name="specialization_id",
            new_name="specialization",
        ),
        migrations.RenameField(
            model_name="like",
            old_name="author_id",
            new_name="author",
        ),
        migrations.RenameField(
            model_name="specialization",
            old_name="specialization",
            new_name="title",
        ),
    ]
