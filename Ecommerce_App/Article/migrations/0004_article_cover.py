# Generated by Django 3.2 on 2023-11-12 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='Article/%Y/%m/%d/', verbose_name='کاور مقاله'),
        ),
    ]