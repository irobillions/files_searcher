import unittest
from unittest.mock import patch

from search.search_by_name import SearchByName


class TestSearchByName(unittest.TestCase):

    def setUp(self):
        self.directories = ['/mocked/dir']
        self.filename = 'testfile'
        self.searcher = SearchByName(self.directories, self.filename)

    @patch('src.search_by_name.os.walk')
    def test_search_file_found(self, mock_os_walk):
        # Mocking os.walk to simulate the file system
        mock_os_walk.return_value = [
            ('/mocked/dir', ['subdir'], ['testfile.txt', 'otherfile.txt']),
            ('/mocked/dir/subdir', [], ['anotherfile.txt'])
        ]

        # Mocking FileInfos
        with patch('src.search.files_infos.FileInfos') as mock_file_infos:
            mock_instance = mock_file_infos.return_value
            mock_instance.to_dict.return_value = {
                'name': 'testfile.txt',
                'path': '/mocked/dir/testfile.txt',
                'summary': ''
            }
            results = self.searcher.search()

            # Verifying the results
            self.assertEqual(len(results), 1)
            self.assertEqual(results[0]['name'], 'testfile.txt')
            self.assertEqual(results[0]['path'], '/mocked/dir/testfile.txt')


if __name__ == '__main__':
    unittest.main()
