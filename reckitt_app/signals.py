# reckitt_app/signals.py

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError

from .models import LineUser

# ตั้งค่า LINE API
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

@receiver(post_save, sender=LineUser)
def notify_line_user_updated(sender, instance, created, **kwargs):
    """ส่งข้อความแจ้งเตือนเมื่อมีการอัพเดตข้อมูลผู้ใช้"""
    if not created and settings.LINE_CHANNEL_ACCESS_TOKEN:
        try:
            # ส่งข้อความแจ้งเตือนเมื่อมีการอัพเดตข้อมูล
            message = f"ข้อมูลของคุณได้รับการอัพเดต โดยแอดมิน:\n"
            
            if instance.first_name or instance.last_name:
                message += f"ชื่อ-นามสกุล: {instance.first_name} {instance.last_name}\n"
            
            if instance.employee_id:
                message += f"รหัสพนักงาน: {instance.employee_id}\n"
                
            if instance.department:
                message += f"แผนก: {instance.department}\n"
                
            line_bot_api.push_message(
                instance.line_id,
                TextSendMessage(text=message)
            )
        except LineBotApiError as e:
            print(f"LINE API Error: {e}")