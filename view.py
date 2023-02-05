from aiogram import types
from bot import bot
import model
import random
from random import choice


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, привет! Это игра в конфетки!\n'
                        'Правила игры:\n'
                        'Первый ход определяется жеребьевкой.\n'
                        'Игроки ходят, совершая ход друг после друга.\n'
                        'Всего на столе 150 конфет.\n'
                        'За один ход можно забрать от 1 до 28 конфет.\n'
                        'Кто заберёт последние конфеты, тот и победил.\n'
                        'Для начала игры ввведи команду /game\n'
                        'Чтобы посмотреть доступные команды, введи /help')

async def the_end(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'Игра окончена. Чтобы начать новую игру, введи команду /game\n'
                        'Если хочешь еще раз прочитать правила - /rules')


async def support(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вот все доступные команды:\n'
                                                 '/start - начало игры\n'
                                                 '/finish - конец игры\n'
                                                 '/game - начать новую игру\n'
                                                 '/help - помощь с командами\n'
                                                 '/rules - правила игры\n')

async def law(message: types.Message):
    await bot.send_message(message.from_user.id, 'Правила игры:\n'
                        'Первый ход определяется жеребьевкой.\n'
                        'Игроки ходят, совершая ход друг после друга.\n'
                        'Всего на столе 150 конфет.\n'
                        'За один ход можно забрать не более 28 конфет\n'
                        'Кто заберёт последние конфеты, тот и победил')

async def play(message: types.Message):
    model.firstPlayer = random.randint(1, 2)
    if model.firstPlayer == 1:
        await message.answer('Ходи первым! Напиши количество конфет')
    else:
        model.count = model.total_count % (model.max_turn + 1)
        model.total_count -= model.count
        await message.answer(f'Я хожу первым и беру {model.count} конфет. Осталось {model.total_count} конфет.\n'
                              'Твой ход!')

async def leftover_candy(message: types.Message):
    await bot.send_message(message.from_user.id, f'Осталось {model.total_count} конфетки')

async def new_game(message: types.Message):
    await bot.send_message(message.from_user.id, 'Для новой игры введи команду /game.\n'
                                                 'Если хочешь еще раз прочитать правила, то введи команду /rules')

async def bot_takes_candy(message: types.Message):
    await bot.send_message(message.from_user.id, f'Я беру {model.count} конфет. Осталось {model.total_count}')

async def bot_winner(message: types.Message):
    await bot.send_message(message.from_user.id, f'Я беру {model.total_count} конфеток и я победил!')

async def chel_winner(message: types.Message):
    await bot.send_message(message.from_user.id, f'Поздравляю,{message.from_user.first_name}, ты победитель!')

messages = ['Ах, ты грязный читер!', 'Почему ты такой умный?',
            'Я вижу, ты победитель по жизни!', 'Возьми нормально конфетку!', 'Ты у мамки математик!', 'Ты такой приколист!']

async def take_number(message: types.Message):
    await bot.send_message(message.from_user.id, f'{choice(messages)}\n'
                                                 'Возьми от 1 до 28 конфет')

async def error(message: types.Message):
    await bot.send_message(message.from_user.id, 'Ты ввёл совсем не то!\n'
                                                 'Попробуй ещё раз.\n'
                                                 'Для просмотра всех команд введи /help')
