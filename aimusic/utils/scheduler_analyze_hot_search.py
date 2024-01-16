import schedule
import time
import subprocess

def run_command():
    command = "python3 /root/django_aimusic/manage.py analyze_hot_search"
    subprocess.run(command, shell=True)

# 每小时整点执行一次任务
schedule.every().hour.at(":02").do(run_command)

while True:
    schedule.run_pending()
    time.sleep(1)
