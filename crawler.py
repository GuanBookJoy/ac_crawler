import re
import urllib
import urllib.request


def get_key(key, source):
    ret = re.findall(key, source)
    return ret


def get_page_html(url):
    html = urllib.request.urlopen(url)
    html_source = html.read().decode('utf-8')
    html.close()
    return html_source


def result(url, key_set):
    html = get_page_html(url)
    ret = dict()
    for key in key_set:
        key_list = get_key(key, html)
        x = len(key_list)
        ret[key] = x
    return ret


print(result("http://www.hit.edu.cn", {"哈工大", "计算学部", "深圳", "研究生"}))

