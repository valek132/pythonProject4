from aiogram import types
import view
import model
import random


async def start(message: types.Message):
    await view.greetings(message)

async def game(message: types.Message):
    await view.play(message)

async def finish(message: types.Message):
    await view.the_end(message)
    model.total_count = 150

async def help(message: types.Message):
    await view.support(message)

async def rules(message: types.Message):
    await view.law(message)

async def getNumber(message: types.Message):
    model.count = message.text
    if model.count.isdigit():
        model.count = int(model.count)
        if 0 < model.count < model.max_turn + 1:
            model.total_count -= model.count
            if model.total_count == 150 and model.firstPlayer == 2:
                await view.new_game(message)
            else:
                if model.max_turn * 2 + 1 >= model.total_count > model.max_turn + 1:
                    await view.leftover_candy(message)
                    model.count = model.total_count - model.max_turn - 1
                    model.total_count -=  model.count
                    await view.bot_takes_candy(message)
                elif model.total_count == 0:
                    await view.chel_winner(message)
                    await view.new_game(message)
                    model.total_count = 150
                elif model.total_count <= model.max_turn:
                    if model.count > model.total_count + model.count:
                        model.total_count += model.count
                        await view.take_number(message)
                    else:
                        await view.bot_winner(message)
                        await view.new_game(message)
                        model.total_count = 150
                else:
                    await view.leftover_candy(message)
                    if model.firstPlayer == 1:
                        model.count = random.randint(1, 28)
                    else:
                        model.count = model.max_turn+1 - model.count
                    model.total_count -=  model.count
                    await view.bot_takes_candy(message)
        else:
            await view.take_number(message)
    else:
       await view.error(message)