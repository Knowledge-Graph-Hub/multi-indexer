from unittest import TestCase, skip, mock

from ..multi_indexer import parent_url

class TestMultiIndexer(TestCase):

    def setUp(self) -> None:
        self.local_path = 'tests/resources/'
