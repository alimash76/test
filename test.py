import time
from datetime import datetime


while True:
     print("hello ", datetime.now().strftime('%a %b %d %Y %H:%M:%S'))
     time.sleep(1)