# Generated by Django 4.0.4 on 2022-07-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_store',
            name='image',
        ),
        migrations.AddField(
            model_name='book_store',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='Book/thumbnail/%Y/%m/%d/'),
        ),
    ]
