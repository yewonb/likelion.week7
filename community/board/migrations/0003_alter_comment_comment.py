# Generated by Django 4.2.21 on 2025-05-25 15:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("board", "0002_alter_comment_created_at_alter_post_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment",
            field=models.TextField(),
        ),
    ]
