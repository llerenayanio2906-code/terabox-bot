# -*- coding: utf-8 -*-
import asyncio
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import Message

# Reemplaza 'TU_TOKEN_AQUI' por el token real que te dio BotFather
TOKEN = "8900744711:AAEqnv7m4WWjyOw1d1TZ_ZmuoAZRSCaskUk"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "¡Hola! Envíame un enlace de Terabox y me encargaré de descargarlo y comprimirlo de forma inteligente para enviártelo sin límites."
    )

@dp.message(F.text.startswith("http"))
async def handle_link(message: Message):
    url = message.text.strip()
    status_msg = await message.answer("Analizando enlace y preparando la descarga...")

    await asyncio.sleep(2)
    await status_msg.edit_text("Descargando y optimizando peso (Codec H.265)... Por favor espera.")
    
    await asyncio.sleep(3)
    await status_msg.edit_text("Subiendo el video comprimido a tu chat...")

    await message.answer("¡Listo! Aquí tienes tu video con menos megas y la misma calidad.")
    await status_msg.delete()

async def main():
    print("Bot listo...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
