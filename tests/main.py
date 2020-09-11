import unittest
from queryStringParser import parser


class TestCaseQueryStringParser(unittest.TestCase):

    def test_parse(self):
        string = "foo[]=bar+foo&foo[]=baz&biz[name]=gino&biz[name]=pino&caz=33&paz[]=ggu"
        result = {'foo': ['bar foo', 'baz'], 'biz': {'name': 'pino'}, 'caz': '33', 'paz': ['ggu']}

        self.assertEqual(parser.parse(string), result)
        pass


if __name__ == '__main__':
    unittest.main()
