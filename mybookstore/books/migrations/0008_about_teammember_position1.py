# Generated by Django 5.0.2 on 2024-02-25 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_about_contactabout_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='TeamMember_position1',
            field=models.CharField(default='', max_length=100),
        ),
    ]
