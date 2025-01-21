from telethon import TelegramClient

# Замените значения на ваши
api_id = 22929626
api_hash = '6a51dc5908d5911406b153f12ab47ca0'
phone_number = '+77020959595'  # Укажите ваш номер в формате +1234567890

# Создаем клиент
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)
    print("Клиент успешно подключен!")
    
    # Пример получения диалогов
    async for dialog in client.iter_dialogs():
        print(f"Чат: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
