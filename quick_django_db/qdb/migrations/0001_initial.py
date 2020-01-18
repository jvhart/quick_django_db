# Generated by Django 2.1 on 2020-01-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=32, null=True)),
                ('last_name', models.CharField(max_length=32)),
                ('person_id', models.IntegerField()),
                ('person_active', models.BooleanField()),
                ('record_create_dt', models.DateTimeField(auto_now=True)),
                ('record_modify_dt', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Example Table Records',
                'verbose_name_plural': 'Example Table Records',
                'db_table': 'example_table',
                'ordering': ['last_name', 'first_name'],
            },
        ),
    ]