# Generated by Django 4.1 on 2022-08-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
                ('brendi', models.CharField(max_length=50)),
                ('narxi', models.IntegerField()),
                ('miqdori', models.IntegerField()),
            ],
        ),
    ]