# 📱 Termux Battery Checker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue) 
![Termux](https://img.shields.io/badge/Termux-Android-brightgreen) 
![License](https://img.shields.io/badge/License-MIT-green)  

**یه اسکریپت ساده، سبک و دوست‌داشتنی برای رفیق‌های قدیمی و نو ❤️**  
*متولد شده روی یک Samsung Galaxy A22 5G افسانه‌ای*

</div>

---

## 🎂 داستان تولد
این اسکریپت روی یه **Galaxy A22 5G** به دنیا اومد؛ همون رفیقی که ۴ سال با هم کد زدیم، فری فایر بازی کردیم و سر 4+5G دعوا داشتیم. 😤  
صفحه‌نمایشش رو با `SetEdit` و انیمیشن `×0` به موشک تبدیل کردیم 🚀 و DPI رو رسوندیم به ۴۲۰ تا موس بچسبه به دستمون 🖱️.  
باتریش "پت پت" می‌کرد، ولی هنوز نمرده بود... این اسکریپت شد شناسنامه افتخارش. 🥲💚

---

## ✨ ویژگی‌ها

| 🧩 ویژگی | توضیح |
|-----------|--------|
| 🆔 **شناسنامه گوشی** | مدل، برند، پردازنده، نسخه‌ی اندروید |
| 🔋 **وضعیت باتری** | درصد شارژ، سلامت، دما، ولتاژ و وضعیت شارژ |
| 🎨 **خروجی رنگی** | قرمز برای داغی، زرد برای ولتاژ پایین |
| ⚠️ **هشدار بحرانی** | اخطار در صورت افت ولتاژ زیر ۳۴۰۰ میلی‌ولت |

---

## 🖥️ پیش‌نیازها

| ابزار | روش نصب |
|--------|-----------|
| **Termux** | از [F-Droid](https://f-droid.org/en/packages/com.termux/) نصب کنید |
| **Python 3** | `pkg install python` |
| **Termux-API** | `pkg install termux-api` |

---

## ⚙️ روش نصب و اجرا

### ۱. کلون از گیت‌هاب
```bash
git clone https://github.com/amiralisalmani-jajarm/tastbateri.git
cd Termux-Battery-Checker
python battery.py
