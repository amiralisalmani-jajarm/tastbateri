#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import json

def get_device_info():
    info = {}
    props = {
        "ro.product.model": "مدل گوشی",
        "ro.product.brand": "برند",
        "ro.product.manufacturer": "سازنده",
        "ro.build.version.release": "نسخه اندروید",
        "ro.build.id": "ساخت شماره",
        "ro.board.platform": "پلتفرم",
        "ro.product.cpu.abi": "معماری CPU"
    }
    for prop, desc in props.items():
        try:
            result = subprocess.run(
                ['getprop', prop],
                capture_output=True, text=True, timeout=5
            )
            value = result.stdout.strip()
            if value:
                info[desc] = value
        except Exception:
            pass
    return info

def get_battery_data():
    try:
        result = subprocess.run(
            ['termux-battery-status'],
            capture_output=True, text=True, timeout=5
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception:
        return None
    return None

def health_emoji(h):
    return {
        "GOOD": "✅ عالیه",
        "COLD": "🥶 سرده",
        "DEAD": "💀 تمومه",
        "OVERHEAT": "🔥 داغه",
        "OVER_VOLTAGE": "⚡ نوسان برق"
    }.get(h, f"❓ {h}")

def voltage_warning(volt):
    v = int(volt)
    if v < 3400:
        return "   ⚠️ هشدار: ولتاژ خیلی پایینه! گوشی رو شارژ کن."
    elif v < 3500:
        return "   🟡 هشدار ملایم: ولتاژ پایینه. بهتره شارژ کنی."
    return ""

# --- اجرای گزارش ---
print("\033[96m" + "="*50 + "\033[0m")
print("\033[1;93m   🆔 شناسنامه گوشی و وضعیت باتری\033[0m")
print("\033[96m" + "="*50 + "\033[0m")

device = get_device_info()
if device:
    print("\033[1;94m📱 مشخصات دستگاه:\033[0m")
    for key, val in device.items():
        print(f"   • {key}: \033[92m{val}\033[0m")
else:
    print("⚠️ نتونستم اطلاعات گوشی رو بخونم.")

print("\n" + "\033[96m" + "="*50 + "\033[0m")

battery = get_battery_data()
if battery:
    print("\033[1;94m🔋 وضعیت باتری:\033[0m")
    print(f"   • درصد شارژ: \033[93m{battery.get('percentage', '?')}%\033[0m")
    
    status = battery.get('status', '?')
    fa = {
        "CHARGING": "⚡ در شارژ",
        "DISCHARGING": "🔌 تخلیه",
        "FULL": "✅ پر",
        "NOT_CHARGING": "🚫 بدون شارژ"
    }
    print(f"   • وضعیت: {fa.get(status, status)}")
    
    health = battery.get('health', 'UNKNOWN')
    print(f"   • سلامت: {health_emoji(health)}")
    
    temp = battery.get('temperature', None)
    if temp:
        t = temp if temp < 50 else temp/10
        color = "\033[91m" if t > 40 else "\033[93m"
        print(f"   • دما: {color}{t:.1f}°C\033[0m")
    
    volt = battery.get('voltage', None)
    if volt:
        print(f"   • ولتاژ: \033[94m{volt} mV\033[0m")
        print(voltage_warning(volt))
else:
    print("❌ اطلاعات باتری در دسترس نیست.")
    print("   با دستور زیر termux-api رو نصب کن:")
    print("   \033[93mpkg install termux-api\033[0m")

print("\033[96m" + "="*50 + "\033[0m")
print("📎 این گزارش رو می‌تونی با دوستات به اشتراک بذاری.")
print("   برای اجرای مجدد: \033[93mpython battery.py\033[0m")