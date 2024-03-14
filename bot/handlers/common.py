from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("cancel"))
@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        text="Ас-саляму алейкум, кош кельдиниз!\nНапишите текст на ногайском, бот сделает транскрипцию на турецкий\n\nEsselamu aleyküm, koş keldiniz!\nMetni Türkçe yazın, bot Latince'ye çevirecektir."
    )
