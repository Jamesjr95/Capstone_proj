# Generated by Django 4.0.1 on 2022-02-18 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0019_character_alighnment_character_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='alighnment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]