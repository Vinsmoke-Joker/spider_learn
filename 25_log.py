import logging


# logging.basicConfig()  # 对日志输出格式进行设置
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='myapp.log',
                    # filemode='w'
                    )
logger = logging.getLogger(__name__)

if __name__=='__main__':
    logger.info('this is a info log ')
    logger.info('this is a info log 1')


