import logging
from comm.handle_path import LOG_DIR
import time
import os


"""
日志模块
"""
class Log:
    @staticmethod
    def create_logger():
        #日志文件的绝对路径
        logname = os.path.join(LOG_DIR, "{}.log".format(time.strftime("%Y_%m_%d")))
        #输出日志格式
        formatter = '%(asctime)s - [%(filename)s -->ling:%(lineno)d] - %(levelname)s: %(message)s'
        fm = logging.Formatter(formatter)

        mylog = logging.getLogger()
        mylog.setLevel(logging.INFO)

        #日志输出到屏幕上
        sh = logging.StreamHandler()
        sh.setLevel(logging.ERROR)
        sh.setFormatter(fm)
        mylog.addHandler(sh)

        #日志输出到文件中
        fh = logging.FileHandler(filename=logname, encoding="utf-8")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(fm)
        mylog.addHandler(fh)

        return mylog
    

log = Log.create_logger()


if __name__ == "__main__":
    print("日志级别(由低到高): DEBUG, INFO, WARNING, EOOR, CRITICAL")
    log.debug("DEBUG - 细节信息, 用于了解Bug是如何产生的")
    log.info("INFO - 确认工作正常")
    log.warning("WARNING - 提示有不期望的事情发生了, 但是预期以内的情况")
    log.error("ERROR - 严重问题, 软件可能无法执行某些功能")
    log.critical("CRITICAL - 更严重的问题, 提示程序自身无法继续运行")