from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Ijaraga olaman"), KeyboardButton(text="Ijaraga beraman")]],
        resize_keyboard=True
    )

def ijara_beraman_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Kvartira"), KeyboardButton(text="Uy / hovli")],
            [KeyboardButton(text="Ofis"), KeyboardButton(text="Dacha")]
        ],
        resize_keyboard=True
    )

def xona_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1 xona"), KeyboardButton(text="2 xona"), KeyboardButton(text="3 xona")],
            [KeyboardButton(text="4 xona"), KeyboardButton(text="5 xona")]
        ],
        resize_keyboard=True
    )

def tuman_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Yunusobod"), KeyboardButton(text="Mirzo Ulug‘bek")],
            [KeyboardButton(text="Chilonzor"), KeyboardButton(text="Mirobod")],
            [KeyboardButton(text="Shayxontohur"), KeyboardButton(text="Uchtepa")],
            [KeyboardButton(text="Olmazor"), KeyboardButton(text="Yashnobod")],
            [KeyboardButton(text="Bektemir"), KeyboardButton(text="Sergeli")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )

def kvadrat_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="10 m²"), KeyboardButton(text="20 m²"), KeyboardButton(text="30 m²")],
            [KeyboardButton(text="40 m²"), KeyboardButton(text="50 m²")]
        ],
        resize_keyboard=True
    )

def jihoz1_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Stol"), KeyboardButton(text="Stul")],
            [KeyboardButton(text="Shkaf"), KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )

def jihoz2_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Kreslo"), KeyboardButton(text="Televizor")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )

def jihoz3_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Dona lamp"), KeyboardButton(text="Divan")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )

def muddat_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Kunlik"), KeyboardButton(text="Uzoq muddat")],
            [KeyboardButton(text="Orqaga")]
        ],
        resize_keyboard=True
    )

def telefon_menyu():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📞 Telefon yuborish", request_contact=True)]],
        resize_keyboard=True
    )