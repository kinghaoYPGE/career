"""
对c5模板的单元测试
"""
import unittest
from c5 import Dict

# 自定义测试用例
class TestDict(unittest.TestCase):

    # 测试需要连接数据库
    def setUp(self):
        print('setUp')

    # 测试需要关闭数据库
    def tearDown(self):
        print('tearDown')

    def test_init(self):
        d = Dict(a=1, b='b')
        # 是否和期望相等
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'b')
        self.assertTrue(isinstance(d, dict))
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        # d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        # d['key'] = 'value'
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
        
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


if __name__ == '__main__':
    unittest.main()