# Generated by Django 3.2 on 2023-09-22 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('zipcode', models.BigIntegerField(verbose_name='zipcode')),
                ('Plaque', models.PositiveIntegerField(blank=True, null=True, verbose_name='Plaque')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Address',
                'db_table': 'Address',
            },
        ),
    ]