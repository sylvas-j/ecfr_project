# Generated by Django 3.2.4 on 2022-08-19 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_subject_subject_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='subject_section',
            field=models.CharField(choices=[('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023'), ('2023/2024', '2023/2024'), ('2024/2025', '2024/2025')], max_length=9, null=True),
        ),
    ]
