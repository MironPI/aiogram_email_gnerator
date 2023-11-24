import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import re
from aiogram import types, Dispatcher
from aiogram.contrib.middlewares.i18n import I18nMiddleware

bot = Bot(token="BOT_TOKEN")  # BOT_TOKEN o'rniga o'zingizning botningizning API kalitini yozing

# Dispatcher va xotira saqlashni o'rnatish
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Elektron pochta manzilini tekshirish uchun funksiya
def is_valid_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email)

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchi haqida ma'lumotlarni olish
    user = message.from_user
    user_id = user.id
    user_email = user.email

    # Foydalanuvchi qayta ro'yxatdan o'tganmi tekshirish
    if user_email:
        await message.reply("Siz allaqachon ro'yxatdan o'tgansiz. Kiring!")
    else:
        await message.reply("Assalomu alaykum! Elektron pochta manzilingizni yuboring.")

# Elektron pochta manzilini qabul qilish
@dp.message_handler(func=lambda message: not is_valid_email(message.text), content_types=types.ContentTypes.TEXT)
async def handle_invalid_email(message: types.Message):
    await message.reply("Noto'g'ri formatdagi elektron pochta manzili. Qaytadan yuboring.")

@dp.message_handler(func=is_valid_email, content_types=types.ContentTypes.TEXT)
async def handle_valid_email(message: types.Message):
    email = message.text
    # Yuborilgan elektron pochta manzili bilan kerakli ishlarni bajarish
    # Masalan, manzilni tekshirish va ishlatish
    await message.reply(f"Elektron pochta manzilingiz: {email}")

if __name__ == '__main__':
    # Kodni boshlash
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)



# Lokalizatsiya sozlamalari
I18N_DOMAIN = 'my_bot'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALES_DIR = os.path.join(BASE_DIR, 'locales')


```python
from datetime import date

# Start komandasi
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Foydalanuvchi haqida ma'lumotlarni olish
    user = message.from_user
    user_id = user.id

    # Foydalanuvchidan tug'ilgan sanasini so'rang
    await message.reply("Assalomu alaykum! Tug'ilgan sanangizni kiriting (sana formati: YYYY-MM-DD).")

@dp.message_handler(regexp=r'^\d{4}-\d{2}-\d{2}$')  # Sana formatini tekshirish
async def handle_birthday(message: types.Message):
    birthday = message.text

    # Tug'ilgan sana va joriy sana orasidagi yoshni hisoblash
    today = date.today()
    birthdate = date.fromisoformat(birthday)
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Foydalanuvchi yoshini tekshirish
    if age < 10 or age > 70:
        await message.reply("Uzr, sizning yoshingizga mos kelmaydigan botdan foydalanish imkoni yo'q.")
    else:
        await message.reply("Assalomu alaykum! Siz botdan foydalanishingiz mumkin.")
