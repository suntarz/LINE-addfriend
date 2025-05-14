# Reckitt LINE Management System

ระบบจัดการผู้ใช้งาน LINE สำหรับ Reckitt บน Django Framework เชื่อมต่อกับ Microsoft SQL Server

## คุณสมบัติ

- รับ webhook จาก LINE เมื่อมีการเพิ่มเพื่อน (Add Friend)
- บันทึกข้อมูลผู้ใช้ LINE ลงฐานข้อมูล Microsoft SQL Server
- จัดการข้อมูลผู้ใช้ (เพิ่ม/แก้ไข/ลบ)
- ค้นหาและกรองผู้ใช้งาน
- ส่งข้อความแจ้งเตือนเมื่อมีการอัพเดตข้อมูลผู้ใช้

## ข้อกำหนดเบื้องต้น

- Python 3.8+
- Django 3.2+
- Microsoft SQL Server
- Microsoft ODBC Driver 17 for SQL Server
- LINE Bot API

## การติดตั้ง

1. โคลนโปรเจคหรือแตกไฟล์โปรเจค:

```bash
git clone <repository-url>
cd reckitt_project
```

2. สร้าง Virtual Environment และติดตั้ง dependencies:

```bash
python -m venv venv
source venv/bin/activate  # สำหรับ Linux/Mac
venv\Scripts\activate     # สำหรับ Windows

pip install -r requirements.txt
```

3. สร้างไฟล์ .env ใน root directory ของโปรเจค:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com

# Database Configuration
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_database_host
DB_PORT=1433

# LINE Bot Configuration
LINE_CHANNEL_ACCESS_TOKEN=your-line-channel-access-token
LINE_CHANNEL_SECRET=your-line-channel-secret
```

4. สร้างฐานข้อมูลและ migrate:

```bash
python manage.py migrate
```

5. สร้าง superuser:

```bash
python manage.py createsuperuser
```

6. รวบรวมไฟล์ static:

```bash
python manage.py collectstatic
```

7. รันเซิร์ฟเวอร์:

```bash
python manage.py runserver
```

## การตั้งค่า LINE Webhook

1. สร้าง LINE Bot ผ่าน [LINE Developers Console](https://developers.line.biz/)
2. ตั้งค่า Webhook URL เป็น `https://your-domain.com/reckitt_app/webhook/`
3. เปิดใช้งาน Event "Follow" และ "Unfollow" ใน Webhook settings
4. เพิ่ม Channel Access Token และ Channel Secret ในไฟล์ .env

## การทดสอบ

1. เปิดบราวเซอร์และไปที่ `http://localhost:8000/reckitt_app/`
2. เพิ่มผู้ใช้ใหม่หรือรอให้มีการเพิ่มเพื่อนผ่าน LINE application
3. ทดสอบการค้นหา, แก้ไข, และลบผู้ใช้

## โครงสร้างโปรเจค

```
reckitt_project/
├── manage.py
├── reckitt_project/        # โปรเจคหลัก
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── reckitt_app/            # แอพพลิเคชัน
    ├── admin.py            # การตั้งค่าหน้า admin
    ├── models.py           # โมเดลข้อมูล
    ├── views.py            # views สำหรับการแสดงผลและ webhook
    ├── urls.py             # URL patterns
    ├── forms.py            # แบบฟอร์มสำหรับการจัดการข้อมูล
    ├── signals.py          # signals สำหรับส่งข้อความเมื่อมีการอัพเดต
    ├── templates/          # เทมเพลตสำหรับหน้าเว็บ
    └── static/             # ไฟล์ static (CSS, JS, รูปภาพ)
```

## เทคโนโลยีที่ใช้

- **Backend**: Django 3.2+
- **Database**: Microsoft SQL Server
- **Frontend**: Bootstrap 5, Font Awesome, JavaScript
- **API**: LINE Messaging API

## สิ่งที่ควรทำเพิ่มเติม (TODO)

- เพิ่มระบบล็อกอิน/ยืนยันตัวตนสำหรับแอดมิน
- เพิ่มการส่งออกข้อมูลในรูปแบบ CSV/Excel
- เพิ่มการอัพโหลดรูปภาพแทนการใช้ URL
- สร้าง Dashboard สำหรับแสดงสถิติ
- สร้าง API สำหรับเชื่อมต่อกับระบบอื่น"# LINE-addfriend" 
