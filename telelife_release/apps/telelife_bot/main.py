from telegram.ext import Application
from apps.telelife_bot.handlers import life
from apps.telelife_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service
def register(application:Application)->None:life.register(application);application.add_error_handler(make_error_handler(fa.ERROR))
def main()->None:run_bot(Service.TELELIFE,register)
if __name__=='__main__':main()
