import logging
from logging.handlers import TimedRotatingFileHandler
import os
import datetime

class DailyTimedRotatingFileHandler(TimedRotatingFileHandler):
    def __init__(self, filename, when='midnight', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None):
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)
        self.suffix = "%Y-%m-%d"
        self.namer = self._daily_namer
        self.rotator = self._daily_rotator

    def _daily_namer(self, default_name):
        # 获取当前日期
        now = datetime.datetime.now()
        # 构建新的文件名
        return f"{now.year:04d}-{now.month:02d}-{now.day:02d}.log"

    def _daily_rotator(self, source, dest):
        # 在日志轮转时添加分隔符
        with open(source, "a") as f:
            f.write("\n" + "-" * 80 + "\n")
            f.write(f"Log file rotated on {datetime.datetime.now()}\n")
            f.write("-" * 80 + "\n")

def configure_logging(log_dir='logs'):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 创建一个根日志记录器
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # 设置日志级别为 DEBUG

    # 创建一个按天滚动的日志处理器
    handler = DailyTimedRotatingFileHandler(
        os.path.join(log_dir, 'app.log'),
        when='midnight',
        interval=1,
        backupCount=30,  # 保留最近 30 天的日志
        encoding='utf-8'
    )

    # 设置日志格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 将处理器添加到根日志记录器
    root_logger.addHandler(handler)

    # 如果需要，可以在这里添加更多的处理器，例如控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    return root_logger

def delete_logs(log_file, days_to_keep):
    if not os.path.exists(log_file):
        return

    now = datetime.datetime.now()
    cutoff_date = now - datetime.timedelta(days=days_to_keep)

    with open(log_file, "r") as f:
        lines = f.readlines()

    with open(log_file, "w") as f:
        in_old_log = False
        for line in lines:
            if line.startswith("-" * 80):
                log_date_str = line.split(" ")[-1].strip()
                log_date = datetime.datetime.strptime(log_date_str, '%Y-%m-%d %H:%M:%S.%f')
                in_old_log = log_date < cutoff_date
            if not in_old_log:
                f.write(line)

# 示例：删除7天前的日志内容
# delete_logs('logs/app.log', 7)
# 初始化全局日志记录器
global_logger = configure_logging()