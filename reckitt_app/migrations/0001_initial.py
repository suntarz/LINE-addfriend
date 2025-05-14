# reckitt_app/migrations/0001_initial.py

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LineUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_id', models.CharField(max_length=50, unique=True, verbose_name='LINE ID')),
                ('display_name', models.CharField(max_length=100, verbose_name='ชื่อที่แสดง')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ชื่อ')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='นามสกุล')),
                ('employee_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='รหัสพนักงาน')),
                ('department', models.CharField(blank=True, max_length=100, null=True, verbose_name='แผนก')),
                ('picture_url', models.URLField(blank=True, null=True, verbose_name='รูปโปรไฟล์')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='เวลาที่สร้าง')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='อัพเดตล่าสุด')),
            ],
            options={
                'verbose_name': 'ผู้ใช้ LINE',
                'verbose_name_plural': 'ผู้ใช้ LINE',
                'ordering': ['-created_at'],
            },
        ),
    ]