# Generated by Django 4.1.4 on 2023-03-12 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcapp', '0004_alter_tablecolumn_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saravanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('name1', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('extra_special', models.CharField(default='No', max_length=100)),
            ],
            options={
                'db_table': 'saravanan',
            },
        ),
    ]
