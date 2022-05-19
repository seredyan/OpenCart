
import datetime
import os
from idlelib import browser


class Logger():
    # new_logs = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"
    new_logs = f"log_{str(datetime.datetime.now())}.log"
    file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../logs1/", new_logs)

    @classmethod
    def _write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_log(cls, browser):#, url: str):
        testname = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {testname}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request URL: {browser.current_url}\n"
        data_to_add += "\n"

        cls._write_log_to_file(data_to_add)