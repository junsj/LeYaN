import os
import time

cmd = 'python manage.py makemigrations'
os.system(cmd)

time.sleep(1)

cmd = 'python manage.py migrate'
os.system(cmd)

input('Press to exit:')



