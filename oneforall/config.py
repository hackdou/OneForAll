# coding=utf-8
"""
OneForAll配置
"""
import os
import sys
import pathlib

import urllib3
from loguru import logger

# 版本信息
# OneForAll处于开发中，会进行版本快速迭代，请每次在使用前进行更新！
oneforall_version = 'v0.0.8#dev'

# 路径设置
oneforall_relpath = pathlib.Path(__file__).parent  # oneforall代码相对路径
oneforall_abspath = oneforall_relpath.resolve()  # oneforall代码绝对路径
oneforall_module_path = oneforall_relpath.joinpath('modules')  # oneforall模块目录
data_storage_path = oneforall_relpath.joinpath('data')  # 数据存放目录
result_save_path = oneforall_relpath.joinpath('results')  # 结果保存目录

# 模块设置
save_module_result = False  # 保存各模块发现结果为json文件(默认False)
enable_all_module = True  # 启用所有模块(默认True)
enable_partial_module = []  # 启用部分模块 必须禁用enable_all_module才能生效
# 只使用ask和baidu搜索引擎收集子域
# enable_partial_module = [('modules.search', 'ask')
#                          ('modules.search', 'baidu')]


# 爆破模块设置
enable_brute_module = False  # 使用爆破模块(默认禁用)
enable_dns_resolve = True  # DNS解析子域(默认True)
enable_http_request = True  # HTTP请求子域(默认True)
enable_wildcard_check = True  # 开启泛解析检测 会去掉泛解析的子域
# 爆破时使用的进程数(根据系统中CPU数量情况设置 不宜大于CPU数量 默认为系统中的CPU数量)
brute_process_num = os.cpu_count()
brute_coroutine_num = 1024  # 爆破时每个进程下的协程数
# 爆破所使用的字典路径 默认data/subdomains.txt
brute_wordlist_path = data_storage_path.joinpath('subnames.txt')
enable_recursive_brute = False  # 是否使用递归爆破(默认禁用)
brute_recursive_depth = 2  # 递归爆破深度(默认2层)
# 爆破下一层子域所使用的字典路径 默认data/next_subdomains.txt
recursive_namelist_path = data_storage_path.joinpath('next_subnames.txt')
enable_fuzz = False  # 是否使用fuzz模式枚举域名
fuzz_rule = ''  # fuzz域名的正则 示例：[a-z][0-9] 第一位是字母 第二位是数字
ips_appear_maximum = 10  # 同一IP集合出现次数超过10认为是泛解析

# 代理设置
enable_proxy = False  # 是否使用代理(全局开关)
proxy_all_module = False  # 代理所有模块
proxy_partial_module = ['GoogleQuery', 'AskSearch', 'DuckDuckGoSearch',
                        'GoogleAPISearch', 'GoogleSearch', 'YahooSearch',
                        'YandexSearch', 'CrossDomainXml',
                        'ContentSecurityPolicy']  # 代理自定义的模块
proxy_pool = [{'http': 'http://127.0.0.1:1080',
               'https': 'https://127.0.0.1:1080'}]  # 代理池
# proxy_pool = [{'http': 'socks5h://127.0.0.1:10808',
#                'https': 'socks5h://127.0.0.1:10808'}]  # 代理池


# 网络请求设置
enable_fake_header = True  # 启用伪造请求头
request_delay = 1  # 请求时延
request_timeout = 30  # 请求超时
request_verify = False  # 请求SSL验证
# 禁用安全警告信息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 搜索模块设置
enable_recursive_search = False  # 递归搜索子域
search_recursive_times = 2  # 递归搜索层数

# DNS解析设置
resolver_nameservers = [
    '119.29.29.29', '182.254.116.116',  # DNSPod
    '180.76.76.76',  # Baidu DNS
    '223.5.5.5', '223.6.6.6',  # AliDNS
    '114.114.114.114', '114.114.115.115'  # 114DNS
    # '8.8.8.8', '8.8.4.4',  # Google DNS
    # '1.0.0.1', '1.1.1.1'  # CloudFlare DNS
    # '208.67.222.222', '208.67.220.220'  # OpenDNS
]  # 指定查询的DNS域名服务器
resolver_timeout = 5.0  # 解析超时时间
resolver_lifetime = 30.0  # 解析存活时间
limit_resolve_conn = 500  # 限制同一时间解析的数量(默认500)

# 请求端口探测设置
default_ports = [80]  # 默认使用
small_ports = [80, 443, 8000, 8080, 8443]
# 可以在这里面添加端口
large_ports = [80, 81, 280, 300, 443, 591, 593, 832, 888, 901, 981, 1010, 1080,
               1100, 1241, 1311, 1352, 1434, 1521, 1527, 1582, 1583, 1944, 2082,
               2082, 2086, 2087, 2095, 2096, 2222, 2301, 2480, 3000, 3128, 3333,
               4000, 4001, 4002, 4100, 4125, 4243, 4443, 4444, 4567, 4711, 4712,
               4848, 4849, 4993, 5000, 5104, 5108, 5432, 5555, 5800, 5801, 5802,
               5984, 5985, 5986, 6082, 6225, 6346, 6347, 6443, 6480, 6543, 6789,
               7000, 7001, 7002, 7396, 7474, 7674, 7675, 7777, 7778, 8000, 8001,
               8002, 8003, 8004, 8005, 8006, 8008, 8009, 8010, 8014, 8042, 8069,
               8075, 8080, 8081, 8083, 8088, 8090, 8091, 8092, 8093, 8016, 8118,
               8123, 8172, 8181, 8200, 8222, 8243, 8280, 8281, 8333, 8384, 8403,
               8443, 8500, 8530, 8531, 8800, 8806, 8834, 8880, 8887, 8888, 8910,
               8983, 8989, 8990, 8991, 9000, 9043, 9060, 9080, 9090, 9091, 9200,
               9294, 9295, 9443, 9444, 9800, 9981, 9988, 9990, 9999, 10000,
               10880, 11371, 12043, 12046, 12443, 15672, 16225, 16080, 18091,
               18092, 20000, 20720, 24465, 28017, 28080, 30821, 43110, 61600]
ports = {'default': default_ports, 'small': small_ports, 'large': large_ports}
verify_ssl = False
# aiohttp 支持 HTTP/HTTPS形式的代理
get_proxy = None  # proxy="http://user:pass@some.proxy.com"
get_timeout = 5 * 60  # http请求探测总超时时间 None或者0则表示不检测超时 默认5分钟
get_redirects = True  # 允许请求跳转
fake_header = True  # 使用伪造请求头

# 限制同一时间打开的连接总数
limit_open_conn = 30  # 默认30

# 限制同一时间在同一个端点((host, port, is_ssl) 3者都一样的情况)打开的连接数
limit_per_host = 0  # 0表示不限制

subdomains_common = {'i', 'w', 'm', 'en', 'us', 'zh', 'w3', 'app', 'bbs',
                     'web', 'www', 'job', 'docs', 'news', 'blog', 'data',
                     'help', 'live', 'mall', 'blogs', 'files', 'forum',
                     'store', 'mobile'}

# 日志配置
# 终端日志输出格式
stdout_fmt = '<cyan>{time:HH:mm:ss,SSS}</cyan> ' \
             '[<level>{level: <5}</level>] ' \
             '<blue>{module}</blue>:<cyan>{line}</cyan> - ' \
             '<level>{message}</level>'
# 日志文件记录格式
logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
              '[<level>{level: <5}</level>] ' \
              '<cyan>{process.name}({process.id})</cyan>:' \
              '<cyan>{thread.name: <10}({thread.id: <5})</cyan> | ' \
              '<blue>{module}</blue>.<blue>{function}</blue>:' \
              '<blue>{line}</blue> - <level>{message}</level>'

log_path = result_save_path.joinpath('oneforall.log')

logger.remove()
logger.level(name='TRACE', no=5, color='<cyan><bold>', icon='✏️')
logger.level(name='DEBUG', no=10, color='<blue><bold>', icon='🐞 ')
logger.level(name='INFOR', no=20, color='<green><bold>', icon='ℹ️')
logger.level(name='ALERT', no=30, color='<yellow><bold>', icon='⚠️')
logger.level(name='ERROR', no=40, color='<red><bold>', icon='❌️')
logger.level(name='FATAL', no=50, color='<RED><bold>', icon='☠️')

if not os.environ.get('PYTHONIOENCODING'):  # 设置编码
    os.environ['PYTHONIOENCODING'] = 'utf-8'

logger.add(sys.stderr, level='INFOR', format=stdout_fmt, enqueue=True)
logger.add(log_path, level='DEBUG', format=logfile_fmt, enqueue=True,
           encoding='utf-8')
