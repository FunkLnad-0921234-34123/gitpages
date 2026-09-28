import os
import json
import time

# لیست آهنگ‌های موجود رو از songs.json قدیمی بخون (اگه بود)
existing = {}
if os.path.exists('songs.json'):
    with open('songs.json', 'r', encoding='utf-8') as f:
        for song in json.load(f):
            existing[song['file']] = song

# فایل‌های صوتی رو تو پوشه uploads پیدا کن
audio_ext = ['.mp3', '.m4a', '.ogg', '.wav', '.flac']
songs = []

for filename in sorted(os.listdir('uploads')):
    if any(filename.lower().endswith(ext) for ext in audio_ext):
        if filename in existing:
            # اگه قبلاً بود، اطلاعات قبلی رو نگه دار
            songs.append(existing[filename])
        else:
            # آهنگ جدید: اسم رو از اسم فایل بساز
            name = os.path.splitext(filename)[0]
            name = name.replace('-', ' ').replace('_', ' ').title()
            songs.append({
                "name": name,
                "file": filename,
                "date": int(time.time())  # تاریخ الان
            })

# مرتب‌سازی: جدیدترین اول
songs.sort(key=lambda x: x.get('date', 0), reverse=True)

# ذخیره تو songs.json
with open('songs.json', 'w', encoding='utf-8') as f:
    json.dump(songs, f, ensure_ascii=False, indent=2)
