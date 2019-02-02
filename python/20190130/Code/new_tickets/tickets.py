"""
爬取12306火车票信息
python3 tickets.py [-gdtkz](from)上海 (to)马鞍山东 (date)2019-02-03
"""
from docopt import docopt
from stations import stations, requests
from prettytable import PrettyTable
import os
doc = '''
    火车票查询工具
    Usage:
        tickets [-gdtkz] <from> <to> <date>
    
    Options:
        -h, --help  显示帮助菜单
        -g          高铁 
        -d          动车
        -t          特快
        -k          快速
        -z          直达
    Example:
        查看所有列车：tickets 上海 北京 2019-01-31
        只看高铁动车：tickets -gd  上海 北京 2019-01-31
    '''
class TrainCollection(object):
    def __init__(self, json_info, options):
        # 解析JSON得到火车班次相关信息
        self.options = options
        self.header = ['车次信息', '发/到时间', '发/到站', '运行时长', '票价信息', '余票']
        self.train_infos = json_info['data']['trainInfos']

    # 解析火车班次信息
    @property
    def trains(self):
        for train in self.train_infos:
            train_code = train['trainCode']
            init_opt = train_code[0].lower()
            if self.options and init_opt not in self.options:
                continue
            train = [
                train_code,
                '\n'.join([train['deptTime'], train['arrTime']]),
                '\n'.join([train['deptStationName'], train['arrStationName']]),
                train['runTime'],
                '\n'.join([seat['seatName']+' ￥'+seat['seatPrice'] for seat in train['seatList']]),
                '\n'.join([seat['seatNum']+' 张' for seat in train['seatList']])
            ]
            yield train
            
        
    def table(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        
        for train in self.trains:
            pt.add_row(train)
        return pt.get_string(), pt.get_html_string()

def main():
    args = docopt(doc)
    dept_station_code = stations.get(args['<from>'])
    dept_date = args['<date>']
    arr_station_code = stations.get(args['<to>'])
    api_url = r'http://api.12306.com/v1/train/trainInfos?arrStationCode={0}&deptDate={1}&deptStationCode={2}&findGD=false'.format(arr_station_code, dept_date, dept_station_code)

    # 得到火车班次信息
    result = requests.get(api_url).json()
    options = ''.join([k for k, v in args.items() if v is True])
    tc = TrainCollection(result, options)
    table_str, table_html = tc.table()
    print(table_str)
    with open('12306.html', 'w') as f:
        f.write(table_html)

if __name__ == '__main__':
    main()
