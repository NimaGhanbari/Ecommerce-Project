# Generated by Django 3.2 on 2023-11-11 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0001_initial'),
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
        migrations.CreateModel(
            name='Article_File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('file_type', models.PositiveSmallIntegerField(choices=[(1, 'ویدیو'), (2, 'تصویر'), (3, 'PDF')])),
                ('fil', models.FileField(upload_to='Article/%Y/%m/%d/', verbose_name='فایل')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('articel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='Article.article', verbose_name='مقاله')),
            ],
            options={
                'verbose_name': 'Article_file',
                'verbose_name_plural': 'Article_files',
                'db_table': 'Article_files',
            },
        ),
    ]
