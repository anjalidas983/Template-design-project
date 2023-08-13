# Generated by Django 4.2.2 on 2023-06-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='travel/img')),
                ('name', models.CharField(max_length=35)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
