# Generated by Django 3.2.18 on 2023-07-19 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0021_auto_20230719_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.TextField()),
                ('service_description', models.TextField()),
            ],
        ),
    ]
