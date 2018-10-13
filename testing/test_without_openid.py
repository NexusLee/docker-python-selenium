# -*- coding: UTF-8 -*-
import unittest
from without_openid import WithoutOpenId

class testWithoutOpenId(unittest.TestCase):
    def test_withoutOpenId(self):
       WithoutOpenId.test()

if __name__ == '__main__':
    unittest.main()