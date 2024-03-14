from aiogram import Router, types
from aiogram.filters import Command

router = Router()


table = """

A – А
Ä – Аь
B – Б
D – Д
E – Э/Е
F – Ф
G – Г
Ğ – Гъ
H – Х
İ – И
I – Ы
J – Ж
K – К
Q – Къ
L – Л
M – М
N – Н
Ñ – Нъ
O – О
Ö – Оь
P – П
R – Р
S – С
Ş – Ш
T – Т
U – У
Ü – Уь
V – В
Y – Й
Z – З"""

@router.message(Command("info"))
async def cmd_start(message: types.Message):
    await message.answer(
        text="Пожелания предложения пишите @kazykan"
    )