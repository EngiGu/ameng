#
#
#
#
#
#
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

SERVER_PORT = 8888

#################################
# 渠道key, 只有匹配了key，才会发送
SEC_KEYS = [
    'own:EHkmdeTvVgzEJADz32ENZC',  # 自己的一系列服务
    'spider_c:TFvkD9enEkvkVUyMVJUYmN',  # 公司的爬虫业务
]
#################################


#
# 各种账号的配置
###########  新浪邮箱  ############
SINA_SMTP_USER = b'dG90YWxjaGVja0BzaW5hLmNvbQ=='
SINA_SMTP_PASS = b"Z3ExOTk0MDUwNw=="
SINA_SMTP_RECEIVERS = [b"c2F5aGV5YUBxcS5jb20="]

###########  Server酱  ############
SERVER_CHAN_KEY = 'SCU30620T7f7c14060cb17921326cbe6eb83344f25b70f4f1e24ab'
