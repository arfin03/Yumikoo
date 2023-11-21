import os
from os import getenv


API_ID = int(getenv("API_ID", "25826048"))
API_HASH = getenv("API_HASH", "b486ee260537697fdfc56b2b61cbc049")
BOT_USERNAME = getenv("BOT_USERNAME", "Matrixs_X_RVA_bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6374070501:AAGP4z2-jXg3qfYpzCOazeHSUAYiNzQvHvQ")
OWNER_ID = int(getenv("OWNER_ID", "6584511650"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6584511650").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Bikash:Bikash@bikash.yl2nhcy.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQGKEwAAnTJ-C83Jk92qOv0EhuA5NoBo-l0dtfLeXegyU4gYFhEhw3BZdGIaiFJo_IZM5xIjqdrACcxcShw1jpBIIwrqnjM67-962hmRaF1M-VDQtwj-jbhrDzDmib_BKFaFhhdCb7uBBHrKye0Yju1JJbHR_rs10PWKa0FbWybXnjaHQ_a3dpraReNNXFe5X69uMHfp1btQzCKw-n_0Gi3cs9-MneQFJ25polmHCG8LYoQHMdwwhBdzMWQc04KlXhCxKmt3dOBv1H5ZFVzdvPZlo64A51vAKQcM-sFToCSu1byf3h269AafzFGRxZiKpqT3Dg-F9b_SttmfUivPb_632eZXiQAAAAGId6yiAA")
