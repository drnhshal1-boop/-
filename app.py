from flask import Flask, render_template

app = Flask(__name__)

# يمكن إضافة البيانات هنا كقائمة لسهولة التعديل مستقبلاً
services_data = [
    {
        "id": "tg-premium",
        "title": "تفعيل تيليجرام المميز (Premium)",
        "description": "احصل على ميزات حصرية: سرعة مضاعفة في التحميل، رفع ملفات بحجم أكبر، تحويل الصوت إلى نص، وشارة التوثيق بجانب اسمك.",
        "icon": "star",
        "category": "telegram",
        "order_link": "https://t.me/B_B_A_W",
        "details_link": "https://t.me/H_E_D_F/5237",
        "color": "bg-blue-500"
    },
    {
        "id": "tg-stars",
        "title": "شحن نجوم تيليجرام (Stars)",
        "description": "العملة الافتراضية الجديدة داخل تيليجرام؛ استخدمها لدعم صناع المحتوى، شراء المنتجات الرقمية، وإرسال الهدايا المميزة.",
        "icon": "zap",
        "category": "telegram",
        "order_link": "https://t.me/B_B_A_W",
        "details_link": "https://t.me/H_E_D_F/3108",
        "color": "bg-yellow-500"
    },
    # ... بقية الخدمات يتم معالجتها في الواجهة الأمامية لتقليل الضغط على السيرفر
]

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')