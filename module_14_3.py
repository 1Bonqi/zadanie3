from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button)
kb.add(button2)
kb.add(button3)

ikb = InlineKeyboardMarkup()
inline_button = InlineKeyboardButton(text='Рассчитать норму каллорий',
                                     callback_data='calories')
inline_button2 = InlineKeyboardButton(text='Формулы расчета',
                                      callback_data='formulas')
ikb.add(inline_button)
ikb.add(inline_button2)

inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
        [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет!Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('формула: 10 x вес + 6,25 x рост - 5 x возраст + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f"Норма каллорий:{10 * float(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5}")
    await state.finish()


@dp.message_handler(text='Купить')
#async def get_buying_list(message):
#with open('files/product1.png', 'rb') as img1:
#    await message.answer_photo(f'Название: Product1 | Описание: описание 1 | Цена: 100', img1)
#with open('files/product2.png', 'rb') as img2:
#    await message.answer_photo(f'Название: Product2 | Описание: описание 2 | Цена: 200', img2)
#with open('files/product3.png', 'rb') as img3:
#    await message.answer_photo(f'Название: Product3 | Описание: описание 3 | Цена: 300', img3)
#with open('files/product4.png', 'rb') as img4:
#    await message.answer_photo(f'Название: Product4 | Описание: описание 4 | Цена: 400', img4)
#await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb)
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'files/product{i}.png', 'rb') as img:
            await message.answer_photo(img, f'Название:Product{i}| Описание: описание {i} | Цена: {i * 100}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text='Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, что бы начать общение")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
