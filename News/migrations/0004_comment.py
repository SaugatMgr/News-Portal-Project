# Generated by Django 4.2.1 on 2023-05-25 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=64)),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='News.post')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
