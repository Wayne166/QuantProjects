import os
from dotenv import load_dotenv

load_dotenv()

print("Binance Key Exist?", bool(os.getenv("BINANCE_API_KEY")))
print("Binance Secret Exist?", bool(os.getenv("BINANCE_API_SECRET")))