# reckitt_app/views.py

import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.conf import settings
from django.contrib import messages

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import FollowEvent, UnfollowEvent, MessageEvent

from .models import LineUser
from .forms import LineUserForm

# ตั้งค่า LINE API
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@method_decorator(csrf_exempt, name='dispatch')
class LineWebhookView(View):
    """รับ webhook events จาก LINE Platform"""
    
    def post(self, request, *args, **kwargs):
        signature = request.META.get('HTTP_X_LINE_SIGNATURE', '')
        body = request.body.decode('utf-8')
        
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponse(status=400)
        
        for event in events:
            if isinstance(event, FollowEvent):
                # เมื่อมีการ add friend
                self._handle_follow_event(event)
            elif isinstance(event, UnfollowEvent):
                # เมื่อมีการ unfollow/block
                self._handle_unfollow_event(event)
        
        return HttpResponse(status=200)
    
    def _handle_follow_event(self, event):
        """จัดการเมื่อมีการ add friend"""
        line_id = event.source.user_id
        
        try:
            # ดึงข้อมูลผู้ใช้จาก LINE API
            profile = line_bot_api.get_profile(line_id)
            
            # สร้างหรืออัพเดตข้อมูลผู้ใช้
            line_user, created = LineUser.objects.update_or_create(
                line_id=line_id,
                defaults={
                    'display_name': profile.display_name,
                    'picture_url': profile.picture_url,
                }
            )
            
            # ส่งข้อความต้อนรับ
            line_bot_api.push_message(
                line_id, 
                [
                    {
                        "type": "text",
                        "text": f"สวัสดีคุณ {profile.display_name} ยินดีต้อนรับ!"
                    }
                ]
            )
        
        except LineBotApiError as e:
            print(f"LINE API Error: {e}")
    
    def _handle_unfollow_event(self, event):
        """จัดการเมื่อมีการ unfollow/block"""
        line_id = event.source.user_id
        
        # อาจจะต้องการเก็บสถานะผู้ใช้แทนที่จะลบข้อมูล
        # แต่ในที่นี้เราลบข้อมูลออกจากฐานข้อมูล
        LineUser.objects.filter(line_id=line_id).delete()


# Views สำหรับการจัดการผู้ใช้งาน
class LineUserListView(ListView):
    """แสดงรายการผู้ใช้ LINE ทั้งหมด"""
    model = LineUser
    template_name = 'reckitt_app/user_list.html'
    context_object_name = 'users'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # ค้นหาข้อความ
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                models.Q(display_name__icontains=search_query) |
                models.Q(line_id__icontains=search_query) |
                models.Q(first_name__icontains=search_query) |
                models.Q(last_name__icontains=search_query) |
                models.Q(employee_id__icontains=search_query)
            )
        
        # กรองตามแผนก
        department = self.request.GET.get('department')
        if department:
            queryset = queryset.filter(department=department)
            
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # เพิ่มรายการแผนกสำหรับการกรอง
        departments = LineUser.objects.exclude(
            department__isnull=True
        ).exclude(
            department__exact=''
        ).values_list('department', flat=True).distinct().order_by('department')
        
        context['departments'] = departments
        
        # ส่งค่าค้นหากลับไปเพื่อแสดงในฟอร์ม
        context['search_query'] = self.request.GET.get('q', '')
        
        return context


class LineUserDetailView(DetailView):
    """แสดงรายละเอียดของผู้ใช้ LINE คนเดียว"""
    model = LineUser
    template_name = 'reckitt_app/user_detail.html'
    context_object_name = 'user'


class LineUserCreateView(CreateView):
    """สร้างข้อมูลผู้ใช้ LINE ใหม่"""
    model = LineUser
    form_class = LineUserForm
    template_name = 'reckitt_app/user_form.html'
    success_url = reverse_lazy('reckitt_app:user_list')
    
    def form_valid(self, form):
        messages.success(self.request, "สร้างข้อมูลผู้ใช้สำเร็จ")
        return super().form_valid(form)


class LineUserUpdateView(UpdateView):
    """อัพเดตข้อมูลผู้ใช้ LINE"""
    model = LineUser
    form_class = LineUserForm
    template_name = 'reckitt_app/user_form.html'
    context_object_name = 'user'
    
    def get_success_url(self):
        return reverse_lazy('reckitt_app:user_detail', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        messages.success(self.request, "อัพเดตข้อมูลผู้ใช้สำเร็จ")
        return super().form_valid(form)


class LineUserDeleteView(DeleteView):
    """ลบข้อมูลผู้ใช้ LINE"""
    model = LineUser
    template_name = 'reckitt_app/user_confirm_delete.html'
    success_url = reverse_lazy('reckitt_app:user_list')
    context_object_name = 'user'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, "ลบข้อมูลผู้ใช้สำเร็จ")
        return super().delete(request, *args, **kwargs)