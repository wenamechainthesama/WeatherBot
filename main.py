from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from config import TOKEN, WEATHER_TOKEN
from keyboards import city_choice_keyboard
from parser import weather_parser, json_parser


async def write_into_FSM(state, fsm_parameter: str, data_to_fill: str):
    async with state.proxy() as data:
        data[fsm_parameter] = data_to_fill


async def send_weather(message, state):
    async with state.proxy() as data:
        weather_json = weather_parser(data['city'], WEATHER_TOKEN)
        if weather_json != 'Error':
            await message.answer(json_parser(weather_json))
            return await state.finish()

    await message.answer('City not found. Try again - /get_weather')
    await state.finish()


bot = Bot(TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())


class Data(StatesGroup):
    city = State()

requests.exceptions.ProxyError: HTTPSConnectionPool(host='www.youtube.com', port=443): Max retries exceeded with url: /results?search_query=maxter (Caused by ProxyError('Cannot connect to proxy.', NewConnectionError('<urllib3.connection.HTTPSConnection object at 0x7f0268c330a0>: Failed to es tablish a new connection: [Errno 111] Connection refused')))
@dispatcher.message_handler(commands=['start'])
async def start_command(message: types.Message):
    name = message.from_user.first_name
    if name is None:
        name = 'guest'

    await message.answer(text=f"""Hi, <em>{name}</em>! To get started use /get_weather command.""",
                         parse_mode='HTML')


@dispatcher.message_handler(commands=['get_weather'])
async def get_weather(message: types.Message):
    await message.answer(text="""If you want to know the weather in the current place please select one down below. """
                              """Otherwise you can type yours.""",
                         reply_markup=city_choice_keyboard)
    await Data.city.set()


@dispatcher.callback_query_handler(state=Data.city)
async def city_callback(callback: types.CallbackQuery, state: FSMContext):
    await write_into_FSM(state, 'city', callback.data)
    await send_weather(callback.message, state)


@dispatcher.message_handler(content_types=['text'], state=Data.city)
async def city_input(message: types.Message, state: FSMContext):
    await write_into_FSM(state, 'city', message.text)
    await send_weather(message, state)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)