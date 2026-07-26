from telegram.ext import Application
from apps.teleworld_bot.handlers import world
from apps.teleworld_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service
def register(application:Application):world.register(application);application.add_error_handler(make_error_handler(fa.ERROR))
def main():run_bot(Service.TELEWORLD,register)
if __name__=='__main__':main()
