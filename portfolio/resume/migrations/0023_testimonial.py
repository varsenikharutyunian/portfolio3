# Generated by Django 3.2.18 on 2023-07-19 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0022_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('proffesion', models.TextField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
