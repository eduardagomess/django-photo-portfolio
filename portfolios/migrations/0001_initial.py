# Generated by Django 3.1.5 on 2021-02-03 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.CharField(max_length=20)),
                ('camera', models.CharField(max_length=20)),
                ('photo_editor', models.TextField()),
                ('photographer', models.CharField(max_length=20)),
                ('contact', models.TextField()),
                ('image', models.FilePathField(path='/img')),
            ],
        ),
    ]
