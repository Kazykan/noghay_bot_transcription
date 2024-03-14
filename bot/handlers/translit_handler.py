from aiogram import F, Router, types

from service.translit_language import translit_language

router = Router()


@router.message(F.text)
async def cmd_start(message: types.Message):
    answer_text = translit_language(message.text)
    await message.answer(
        text=answer_text
    )