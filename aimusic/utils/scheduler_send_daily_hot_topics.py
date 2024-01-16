import schedule
import time
import subprocess

def run_command():
    command = "python3 /root/django_aimusic/manage.py send_daily_hot_topics"
    subprocess.run(command, shell=True)

# 每天0点执行一次任务
schedule.every(1).day.at("11:08").do(run_command)

while True:
    schedule.run_pending()
    time.sleep(1)

