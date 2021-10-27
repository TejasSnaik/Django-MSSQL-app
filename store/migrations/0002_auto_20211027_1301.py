# Generated by Django 3.2.8 on 2021-10-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specifications',
            name='Categories',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Sports', 'Sports')], max_length=20),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='Products',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='specifications',
            name='SubCategories',
            field=models.CharField(choices=[('Laptop', 'Laptop'), ('Mobile', 'Mobile'), ('Tennis', 'Tennis'), ('Cricket', 'Cricket')], max_length=20),
        ),
    ]
