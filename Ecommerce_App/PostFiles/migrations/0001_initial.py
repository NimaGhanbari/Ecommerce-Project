# Generated by Django 3.2 on 2023-09-22 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('file_type', models.PositiveSmallIntegerField(choices=[(1, 'video'), (2, 'image')], verbose_name='file type')),
                ('fil', models.FileField(upload_to='products/%Y/%m/%d/', verbose_name='file')),
                ('is_active', models.BooleanField(default=True, verbose_name='is enable')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='Product.products', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'db_table': 'files',
            },
        ),
    ]