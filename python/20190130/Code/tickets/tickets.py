"""
爬取12306火车票信息
python3 tickets.py [-gdtkz](from)上海 (to)马鞍山东 (date)2019-02-03
"""
from docopt import docopt
from stations import stations, requests
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
    r = requests.get(base_url, params=params_dict)
    print(r.url)
if __name__ == '__main__':
    main()