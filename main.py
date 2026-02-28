import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from keyboards import (
    main_menu, ijara_beraman_menyu, xona_menyu, tuman_menyu,
    kvadrat_menyu, jihoz1_menyu, jihoz2_menyu, jihoz3_menyu,
    muddat_menyu, telefon_menyu
)
from aiogram.client.session.aiohttp import AiohttpSession


PROXY_URL = 'http://proxy.server:3128'
session = AiohttpSession(proxy=PROXY_URL)

from database import create_db, save_to_db


API_TOKEN = "8756438916:AAH0PKpxszlao4ixhUCbyBO7FLqoqbeHX5k"

logging.basicConfig(level=logging.INFO)

# bot = Bot(token=API_TOKEN)
dp = Dispatcher()
bot = Bot(token=API_TOKEN, session=session)


class IjaraBerish(StatesGroup):
    tur = State()
    xona = State()
    tuman = State()
    kvadrat = State()
    jihoz1 = State()
    jihoz2 = State()
    jihoz3 = State()
    muddat = State()
    narx = State()
    rasm = State()
    telefon = State()


@dp.message(Command("start"))
async def start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Botga xush kelibsiz 😊", reply_markup=main_menu())


@dp.message(F.text == "Ijaraga beraman")
async def beraman_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await message.answer("Siz allaqachon jarayondasiz! ✅")
        return

    await message.answer(
        "Qanday turdagi binoni ijaraga berasiz?\nTugmalardan birini tanlang 👇",
        reply_markup=ijara_beraman_menyu()
    )
    await state.set_state(IjaraBerish.tur)


@dp.message(IjaraBerish.tur)
async def tur_handler(message: types.Message, state: FSMContext):
    await state.update_data(tur=message.text)

    if message.text in ["Kvartira", "Uy / hovli", "Dacha"]:
        await message.answer("Necha xona bo'lsin?", reply_markup=xona_menyu())
        await state.set_state(IjaraBerish.xona)

    elif message.text == "Ofis":
        await message.answer("Kvadrat metrini tanlang 👇", reply_markup=kvadrat_menyu())
        await state.set_state(IjaraBerish.kvadrat)


@dp.message(IjaraBerish.xona)
async def xona_handler(message: types.Message, state: FSMContext):
    await state.update_data(xona=message.text)
    await message.answer("Qaysi tumanda bo'lsin?", reply_markup=tuman_menyu())
    await state.set_state(IjaraBerish.tuman)


@dp.message(IjaraBerish.tuman)
async def tuman_handler(message: types.Message, state: FSMContext):
    await state.update_data(tuman=message.text)
    await message.answer("Kvadrat metrini tanlang 👇", reply_markup=kvadrat_menyu())
    await state.set_state(IjaraBerish.kvadrat)


@dp.message(IjaraBerish.kvadrat)
async def kvadrat_handler(message: types.Message, state: FSMContext):
    await state.update_data(kvadrat=message.text)
    await message.answer(
        "Binoda bor qo'shimcha jihozlarni tanlang 1️⃣ 👇",
        reply_markup=jihoz1_menyu()
    )
    await state.set_state(IjaraBerish.jihoz1)


@dp.message(IjaraBerish.jihoz1)
async def jihoz1_handler(message: types.Message, state: FSMContext):
    await state.update_data(jihoz1=message.text)
    await message.answer(
        "Binoda bor qo'shimcha jihozlarni tanlang 2️⃣ 👇",
        reply_markup=jihoz2_menyu()
    )
    await state.set_state(IjaraBerish.jihoz2)


@dp.message(IjaraBerish.jihoz2)
async def jihoz2_handler(message: types.Message, state: FSMContext):
    await state.update_data(jihoz2=message.text)
    await message.answer(
        "Binoda bor qo'shimcha jihozlarni tanlang 3️⃣ 👇",
        reply_markup=jihoz3_menyu()
    )
    await state.set_state(IjaraBerish.jihoz3)


@dp.message(IjaraBerish.jihoz3)
async def jihoz3_handler(message: types.Message, state: FSMContext):
    await state.update_data(jihoz3=message.text)
    await message.answer("Muddatni tanlang 👇", reply_markup=muddat_menyu())
    await state.set_state(IjaraBerish.muddat)


@dp.message(IjaraBerish.muddat)
async def muddat_handler(message: types.Message, state: FSMContext):
    await state.update_data(muddat=message.text)
    await message.answer("Narxini kiriting 💰 (masalan: 500$ yoki 5 000 000 so'm)")
    await state.set_state(IjaraBerish.narx)


@dp.message(IjaraBerish.narx)
async def narx_handler(message: types.Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("Iltimos 1 ta rasm yuboring 📸", reply_markup=ReplyKeyboardRemove())
    await state.set_state(IjaraBerish.rasm)


@dp.message(IjaraBerish.rasm, F.photo)
async def rasm_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer("Telefon raqamingizni yuboring 👇", reply_markup=telefon_menyu())
    await state.set_state(IjaraBerish.telefon)


@dp.message(IjaraBerish.telefon, F.contact)
async def telefon_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()

    await save_to_db(data, message.contact.phone_number)

    caption = (
        "✅ E'lon kiritildi!\n\n"
        f"🏢 Tur: {data.get('tur')}\n"
        f"🏠 Xona: {data.get('xona')}\n"
        f"📍 Tuman: {data.get('tuman')}\n"
        f"📐 Kvadrat: {data.get('kvadrat')}\n"
        f"🛋 Jihoz1: {data.get('jihoz1')}\n"
        f"🛋 Jihoz2: {data.get('jihoz2')}\n"
        f"🛋 Jihoz3: {data.get('jihoz3')}\n"
        f"⏳ Muddat: {data.get('muddat')}\n"
        f"💰 Narx: {data.get('narx')}\n"
        f"📞 Telefon: {message.contact.phone_number}"
    )

    await message.answer_photo(
        photo=data.get("photo"),
        caption=caption,
        reply_markup=main_menu()
    )

    await state.clear()


async def main():
    await create_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())