import logging
logging.basicConfig(
    filename='milestone1A_logs.txt',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)06d;%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='w'
)
# logging.basicConfig(filename='milestone1A_logs.txt',format='%(asctime)s;  %(message)s',filemode='w')
logger  = logging.getLogger()
logger.setLevel(logging.DEBUG)

