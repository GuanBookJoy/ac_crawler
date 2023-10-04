import urllib
import urllib.request

from adt.Automaton import Automaton


def get_page_html(url):
    html = urllib.request.urlopen(url)
    html_source = html.read().decode('utf-8')
    html.close()
    return html_source


# 初始化自动机
pattern_list = ["深圳", "研究生", "计算学部", "哈工大", "哈尔滨", "哈尔滨工业大学", "学期"]  # 模式集
acp = Automaton()

for pattern in pattern_list:
    acp.add_pattern(pattern)

acp.cal_fail()


# 爬取网页
text = get_page_html("http://www.hit.edu.cn")


# 多模式匹配
result = acp.run_ac(text)


# 打印结果
for i in result.keys():
    print(pattern_list[i - 1], result[i])

