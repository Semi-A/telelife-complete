"""TeleWorld bot entrypoint."""
from __future__ import annotations
from telegram.ext import Application
from apps.teleworld_bot.handlers import onboarding
from apps.teleworld_bot.texts import fa
from packages.core.bot import make_error_handler,run_bot
from packages.core.settings import Service
def register(application:Application)->None:
 onboarding.register(application);application.add_error_handler(make_error_handler(fa.ERROR))
def main()->None:run_bot(Service.TELEWORLD,register)
if __name__=='__main__':main()