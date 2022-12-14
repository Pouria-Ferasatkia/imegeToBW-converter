# Generated by Django 4.1.2 on 2022-10-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0002_remove_file_remark_file_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('file_bw', models.FileField(blank=True, null=True, upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('time', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
