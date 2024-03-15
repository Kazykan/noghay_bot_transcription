from transliterate.base import TranslitLanguagePack, registry
from transliterate import get_available_language_codes, translit

from service.determine_language import determine_language


class TurkishLanguagePack(TranslitLanguagePack):
    language_code = "turkish"
    language_name = "Turkish"
    mapping = (
        "АБДЭEФГХИЫЖКЛМНОПРСШТУВЙЗЮабдэфгхиыжклмнопрсштувйзею",
        "ABDEEFGHİIJKLMNOPRSŞTUVYZÛabdefghiıjklmnoprsştuvyzeû",
    )
    pre_processor_mapping = {
        "Аь": "Ä",
        "Гъ": "Ğ",
        "Къ": "Q",
        "Нъ": "Ñ",
        "Оь": "Ö",
        "Уь": "Ü",
        "аь": "ä",
        "гъ": "ğ",
        "къ": "q",
        "нъ": "ñ",
        "оь": "ö",
        "уь": "ü",
        "Я": "Ya",
        "я": "ya",
    }


registry.register(TurkishLanguagePack)


def translit_language(text: str):
    if determine_language(text) == "turkish":
        return translit(text, language_code="turkish", reversed=True)
    elif determine_language(text) == "russian":
        return translit(text, language_code="turkish")
    else:
        return "Язык не определен нужно, чтобы первый символ в тексте был на русском или турецком\nDil tanımlanmamış, metindeki ilk karakter Rusça veya Türkçe olmalıdır"