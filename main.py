import asyncio
from env import ENV
from aiogram import F, Router
from aiogram import Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.types import Message, chat_permissions, InlineKeyboardButton, InlineKeyboardMarkup
import datetime
from aiogram.utils.keyboard import InlineKeyboardBuilder


router=Router()


@router.message(F.chat.id.in_(set(ENV.CHAT_ID_CONTROL)), F.from_user.id.in_(set(ENV.USERS_ID_CONTROL)))
async def chat_member_res(message: Message,bot: Bot):
    await message.delete()
    await bot.restrict_chat_member(message.chat.id,message.from_user.id, chat_permissions.ChatPermissions())

# @router.message(Text(text="get_chat"))
# async def get_chat_member(message: Message, bot: Bot):
#     a=await bot.create_chat_invite_link(-1001330246156,expire_date=datetime.datetime.now()+datetime.timedelta(days=30),member_limit=1)
#     inline=InlineKeyboardButton(text="ссылка", url=a.invite_link)
#     await bot.unban_chat_member(-1001330246156,message.from_user.id,True)
#     await message.answer(text="ссылка", reply_markup=InlineKeyboardBuilder().add(inline).as_markup())
#     print(a.invite_link)
#     print(await bot.get_chat_member(-1001330246156,message.from_user.id))
#     await bot.unban_chat_member(-1001928027393,message.from_user.id,only_if_banned=True)



@router.message(Command('start'))
async def start_command(message: Message):
    await message.answer("This is control bot")

async def main():
    bot: Bot = Bot(token=ENV.BOT_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

