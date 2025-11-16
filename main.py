
import tkinter as tk
import logging
from app.app import App


app = App()
logger = logging.getLogger(__name__)
print("Welcome to Tasks Manager v0.1.0")
logger.info("Init app...")
app.running()

