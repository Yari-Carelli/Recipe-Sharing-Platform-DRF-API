# Generated by Django 3.2.16 on 2022-12-17 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
