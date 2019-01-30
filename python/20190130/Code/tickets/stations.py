import requests
import re
station_url = r'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9091'
js = requests.get(station_url).text
# @bjb|北京北|VAP|beijingbei|bjb|
stations = dict(re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', js))
