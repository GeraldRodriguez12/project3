# Generated by Django 3.1 on 2020-10-07 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LIST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='INFO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CRUD2.list')),
            ],
        ),
    ]
