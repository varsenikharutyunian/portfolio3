# Generated by Django 3.2.18 on 2023-07-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0024_delete_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField(max_length=30)),
                ('position', models.TextField(max_length=70)),
                ('testimonial', models.TextField(max_length=300)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
