from telegram import BotCommandScopeAllGroupChats,BotCommandScopeAllPrivateChats
from telegram.ext import Application
from apps.telelife_bot.handlers import life
from apps.telelife_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service

async def post_init(application:Application)->None:
 await application.bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
 await application.bot.delete_my_commands(scope=BotCommandScopeAllGroupChats())
def register(application:Application)->None:life.register(application);application.post_init=post_init;application.add_error_handler(make_error_handler(fa.ERROR))
def main()->None:run_bot(Service.TELELIFE,register)
if __name__=='__main__':main()
