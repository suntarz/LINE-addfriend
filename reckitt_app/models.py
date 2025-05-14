# reckitt_app/models.py

from django.db import models
from django.utils import timezone

class LineUser(models.Model):
    """โมเดลสำหรับผู้ใช้งาน LINE"""
    line_id = models.CharField(max_length=50, unique=True, verbose_name="LINE ID")
    display_name = models.CharField(max_length=100, verbose_name="ชื่อที่แสดง")
    first_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="ชื่อ")
    last_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="นามสกุล")
    employee_id = models.CharField(max_length=20, blank=True, null=True, verbose_name="รหัสพนักงาน")
    department = models.CharField(max_length=100, blank=True, null=True, verbose_name="แผนก")
    picture_url = models.URLField(blank=True, null=True, verbose_name="รูปโปรไฟล์")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="เวลาที่สร้าง")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="อัพเดตล่าสุด")
    
    class Meta:
        verbose_name = "ผู้ใช้ LINE"
        verbose_name_plural = "ผู้ใช้ LINE"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.display_name} ({self.line_id})"