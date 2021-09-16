# Generated by Django 3.2.6 on 2021-09-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conexs_pool_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=255)),
                ('db_name', models.CharField(max_length=255)),
                ('db_type', models.CharField(choices=[('Posgresql', 'Posgresql'), ('Mysql', 'Mysql'), ('SqlServer', 'SqlServer')], max_length=255)),
                ('puerto', models.IntegerField()),
                ('active', models.BooleanField()),
            ],
        ),
    ]
