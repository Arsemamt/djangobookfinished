# Generated by Django 5.0.2 on 2024-02-25 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_about_teammember_position1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='ContactAbout_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='TeamMember_position1',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
