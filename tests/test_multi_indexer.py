from unittest import TestCase, skip, mock
from parameterized import parameterized

from multi_indexer import map_file_to_url, parent_url

class TestMultiIndexer(TestCase):

    def setUp(self) -> None:
        self.local_path = 'tests/resources/'

    @parameterized.expand([
        ('/home/', '/home/example/dir', "origin.txt",'/',
            {'name': 'origin.txt', 'url': '/example/dir/origin.txt'}),
        ('~/', '~/example/dir', "design.txt",'/',
            {'name': 'design.txt', 'url': '/example/dir/design.txt'}),
        ('/home/example/', '/example/dir', "virtue.txt",'/',
            {'name': 'virtue.txt', 'url': 'example/dir/virtue.txt'}),
        ('/home/example/', '/example/dir/', "medicine.tz",'/',
            {'name': 'medicine.tz', 'url': 'example/dir/medicine.tz'}),
        ('/home///feign/', '/dir/', "ribbon",'/feign/',
            {'name': 'ribbon', 'url': 'dir/ribbon'})
    ])
    def test_map_file_to_url(self, rootdir, currdir, fname, prefix, expected):
        self.assertEqual(map_file_to_url(rootdir, currdir, fname, prefix),
                        expected)

    @parameterized.expand([
        ('/home/', '/home/example/dir'  ,'/','/example/index.html'),
        ('~/', '~/example/dir'  ,'/','/example/index.html'),
        ('/home/example/', '/example/dir'  ,'/','example/index.html'),
        ('/home/example/', '/example/dir/'  ,'/','example/index.html'),
        ('/home///feign/', '/dir/'  ,'/feign/','index.html')
    ])
    def test_parent_url(self, rootdir, currdir, prefix, expected):
        self.assertEqual(parent_url(rootdir, currdir, prefix),
                        expected)
