# Generated by Django 4.1.2 on 2022-10-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0002_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(),
        ),
    ]
