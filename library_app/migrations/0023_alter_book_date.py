# Generated by Django 4.0.1 on 2022-02-21 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0022_alter_book_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(),
        ),
    ]