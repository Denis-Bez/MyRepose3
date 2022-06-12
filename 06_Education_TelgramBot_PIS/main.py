from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN

import asyncio

# Запуск цикла событий для работы асинхронных функций
loop = asyncio.get_event_loop()

bot = Bot(BOT_TOKEN, parse_mode='HTML') # Принцип форматирования текста, как в HTML (Есть ещё Markdown)
dp = Dispatcher(bot, loop=loop) # Обработчик и доставщик

# Если имя этого файла 'main'. Т.е. мы как бы изолируем при мипортировании код ниже этой надписи
if __name__ == '__main__':
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin) # Функция которая делает запросы getUpdates и передает их в Dispatcher. При запуске выполняет функцию send_to_admin


# Остановился на 8: 03 https://www.youtube.com/watch?v=Ja2vJWcfPyg&list=PLwVBSkoL97Q3phZRyInbM4lShvS1cBl-U&index=3
# Разобраться с ошибкой при запуске: DeprecationWarning: There is no current event loop