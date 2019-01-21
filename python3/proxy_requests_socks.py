"""使用requests请求socks代理服务器
请求http和https网页均适用
"""

import requests

# 要访问的目标网页
page_url = "https://dev.kdlapi.com/testproxy"

# 代理服务器 提示：生成api链接时代理类型请勾选socks4/socks5
proxy = "59.38.241.25:23916"

# 用户名和密码(私密代理/独享代理)
username = "myusername"
password = "mypassword"

proxies = {
    'http': 'socks5://%s:%s@%s' % (username, password, proxy),
    'https': 'socks5://%s:%s@%s' % (username, password, proxy),
    # 提示：如果希望在代理服务器上进行dns解析，把socks5替换成socks5h
}

headers = {
    "Accept-Encoding": "gzip",  # 使用gzip压缩传输数据让访问更快
}


r = requests.get(page_url, proxies=proxies, headers=headers)

print(r.status_code)  # 获取Response的返回码

if r.status_code == 200:
    print(r.text)
