# Generated by Django 5.0.1 on 2024-01-09 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='user',
            name='emailornumber',
            field=models.CharField(blank=True, default='', max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=1, max_length=254, verbose_name='email address'),
            preserve_default=False,
        ),
    ]
