# Generated by Django 3.2.18 on 2023-07-16 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0018_education_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='compani_logo',
        ),
    ]
