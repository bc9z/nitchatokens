import requests
import random
import time

# وظيفة للحصول على بريد إلكتروني مؤقت من Mailinator
def get_temp_email():
    try:
        # استخدام API الخاصة بـ Mailinator للحصول على بريد إلكتروني مؤقت
        response = requests.get('https://api.mailinator.com/v2/domains/public/inboxes?token=<YOUR_API_TOKEN>')
        if response.status_code == 200:
            inbox = response.json()[0]['address']
            return inbox
        else:
            raise Exception("Failed to fetch temp email")
    except Exception as e:
        print(f"Error while fetching temp email: {e}")
        return None

# وظيفة لإنشاء حساب وهمي باستخدام البريد المؤقت
def create_account(proxy):
    try:
        email = get_temp_email()
        if not email:
            return None

        # استخدام بروكسيات لإرسال البيانات
        proxies = {
            "http": f"http://{proxy}",
            "https": f"https://{proxy}",
        }

        # هنا يمكنك إضافة الكود لإنشاء الحساب باستخدام البريد المؤقت
        payload = {
            'email': email,
            'password': 'Password123',  # يمكن أن تضيف معايير أخرى
        }

        # مثال إرسال بيانات لإنشاء الحساب (مثال فقط)
        response = requests.post('https://example.com/create_account', data=payload, proxies=proxies)
        if response.status_code == 200:
            print(f"Account created successfully with email: {email}")
            return email
        else:
            print(f"Failed to create account for {email}")
            return None
    except Exception as e:
        print(f"Error during account creation: {e}")
        return None

# وظيفة لإنشاء عدة حسابات باستخدام بروكسيات
def create_multiple_accounts(proxy_list, num_accounts=10):
    created_accounts = []
    for _ in range(num_accounts):
        # اختيار بروكسي عشوائي من القائمة
        proxy = random.choice(proxy_list)
        print(f"Using proxy: {proxy}")
        email = create_account(proxy)
        if email:
            created_accounts.append(email)
        time.sleep(2)  # تأخير بين الطلبات لتجنب حظر IP
    return created_accounts

# قائمة من البروكسيات التي يمكن استخدامها
proxies_list = [
    "20.210.113.32:8123",
    "50.207.199.81:80",
    "50.172.75.114:80",
    "20.24.43.214:80",
    "50.169.222.243:80"
]

# إنشاء 5 حسابات وهمية باستخدام البروكسيات
created_emails = create_multiple_accounts(proxies_list, num_accounts=5)
print("Created emails:", created_emails)
