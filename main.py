import re
import os
import time as time

filepath = os.path.join('/','share','Projects', 'gpi_0.7_hw_reworked')
filename = 'autoreload.py'
file = os.path.join(filepath, filename)
# file = filename
# print(file)

time.sleep(5)

with open(file, 'w') as writer:
    writer.seek(0)
    writer.writelines(['# Now you see me\n'])

with open(file, 'w') as writer:
    writer.seek(0)
    writer.writelines(["# Now you don't\n"])

