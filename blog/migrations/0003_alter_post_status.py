# Generated by Django 3.2 on 2021-05-04 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[('0', 'Draft'), ('1', 'Published')], default=0),
        ),
    ]
