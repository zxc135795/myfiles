# Generated by Django 3.0.3 on 2020-02-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_book_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]