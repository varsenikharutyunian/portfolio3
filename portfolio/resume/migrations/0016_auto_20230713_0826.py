# Generated by Django 3.2.18 on 2023-07-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0015_delete_fact'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='university_name',
            field=models.TextField(),
        ),
    ]
