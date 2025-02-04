# Generated by Django 5.0.1 on 2025-02-03 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_movie_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, default='data:image/jpeg;base64,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', null=True, upload_to='movie_images/'),
        ),
    ]
