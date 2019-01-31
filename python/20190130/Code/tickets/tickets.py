"""
爬取12306火车票信息
python3 tickets.py [-gdtkz](from)上海 (to)马鞍山东 (date)2019-02-03
"""
from docopt import docopt
from stations import stations, requests
from prettytable import PrettyTable
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
        tickets 上海 北京 2019-01-31
        tickets -g  上海 北京 2019-01-31
    '''
class TrainCollection(object):
    header = '车次|车站|时间|耗时|一等座|二等座|高级软卧|软卧|硬卧|硬座|无座'.split(r'|')
    indexs = '3|6|8|10|-6|-7|-8|-9|-10|-11|-12'.split(r'|')
    
    def __init__(self, free_trains, free_place, options):
        self.free_trains = free_trains
        self.free_place = free_place
        self.options = options

    # 解析火车班次信息
    @property
    def trains(self):
        for train in self.free_trains:
            train_info_list = train.split(r'|')
            train_no = train_info_list[3]
            init_opt = train_no[0].lower()
            # 生成器减少内存开销
            yield [train_info_list[int(index)] for index in self.__class__.indexs \
            if not self.options or init_opt in self.options]
        
    def table(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        return pt

def main():
    args = docopt(doc)
    base_url = r'https://kyfw.12306.cn/otn/leftTicket/queryZ'
    train_date = args['<date>']
    from_station = stations.get(args['<from>'])
    to_station = stations.get(args['<to>'])
    params_dict = {}
    params_dict['leftTicketDTO.train_date'] = train_date
    params_dict['leftTicketDTO.from_station'] = from_station
    params_dict['leftTicketDTO.to_station'] = to_station
    params_dict['purpose_codes'] = 'ADULT'
    # 火车班次字典
    r = requests.get(base_url, params=params_dict).json()
    free_trains = r['data']['result']
    free_place = r['data']['map']
    options = ''.join([k for k, v in args.items() if v is True])

    # 解析火车班次信息并以表格形式打印到控制台
    trains = TrainCollection(free_trains, free_place, options)
    table = trains.table()
    print(table)

def run():
    args = docopt(doc)
    print(args)

if __name__ == '__main__':
    run()