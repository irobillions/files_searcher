import sys
import os
import pytest
from unittest.mock import patch, MagicMock

from search.search_by_name import SearchByName

@pytest.fixture
def search_by_name():
    directories = ['/mocked/dir']
    filename = 'testfile'
    return SearchByName(directories, filename)

@patch('search.search_by_name.os.walk')
def test_search_file_found(mock_os_walk, search_by_name):
    # Mocking os.walk pour simuler le système de fichiers
    mock_os_walk.return_value = [
        ('/mocked/dir', ['subdir'], ['testfile.txt', 'otherfile.txt']),
        ('/mocked/dir/subdir', [], ['anotherfile.txt'])
    ]

    # Mocking FileInfos
    with patch('search.search_by_name.FileInfos') as mock_file_infos:
        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.return_value = {
            'name': 'testfile.txt',
            'path': '/mocked/dir/testfile.txt',
            'summary': ''
        }
        results = search_by_name.search()

        # Vérification des résultats
        assert len(results) == 1
        assert results[0]['name'] == 'testfile.txt'
        assert results[0]['path'] == '/mocked/dir/testfile.txt'



@patch('search.search_by_name.os.walk')
def test_search_file_not_found(mock_os_walk, search_by_name):
    mock_os_walk.return_value = [
        ('/mocked/dir', ['subdir'], ['otherfile.txt']),
        ('/mocked/dir/subdir', [], ['anotherfile.txt'])
    ]

    results = search_by_name.search()
    assert len(results) == 0


@patch('search.search_by_name.os.walk')
def test_search_directory_not_found(mock_os_walk, search_by_name):

    mock_os_walk.return_value =  [
            ('/mocked/dir', ['testfile'], ['otherfile.txt']),
            ('/mocked/dir/testfile', [], ['anotherfile.txt'])
        ]


    with patch("search.search_by_name.FileInfos") as mock_file_infos:
        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.return_value = {
            'name': 'testfile',
            'path': '/mocked/dir/testfile',
            'summary': ''
        }

        results = search_by_name.search()

        assert len(results) == 1
        assert results[0]['name'] == 'testfile'
        assert results[0]['path'] == '/mocked/dir/testfile'


if __name__ == '__main__':
    pytest.main()
