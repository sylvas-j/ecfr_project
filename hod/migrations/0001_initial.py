# Generated by Django 3.2.4 on 2022-07-14 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_no', models.CharField(max_length=15, unique=True)),
                ('hod_gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=8, null=True)),
                ('active', models.BooleanField(default=0, max_length=1)),
                ('hod_reg', models.DateField(auto_now_add=True)),
                ('hod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HodCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hod_reg', models.DateField(auto_now_add=True)),
                ('courses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='subjects.subject')),
                ('hod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hod.hod')),
            ],
        ),
    ]
