from telegram import BotCommandScopeAllGroupChats,BotCommandScopeAllPrivateChats
from telegram.ext import Application
from apps.teleworld_bot.handlers import world
from apps.teleworld_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service

async def post_init(application:Application)->None:
 await application.bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
 await application.bot.delete_my_commands(scope=BotCommandScopeAllGroupChats())
def register(application:Application):world.register(application);application.post_init=post_init;application.add_error_handler(make_error_handler(fa.ERROR))
def main():run_bot(Service.TELEWORLD,register)
if __name__=='__main__':main()
