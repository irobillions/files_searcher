import sys
import os
import pytest
from unittest.mock import patch, MagicMock

from search.search_by_name import SearchByNameStrategy
from search.search_by_type import SearchByTypeStrategy

@pytest.fixture
def search_by_name_strategy():
    return SearchByNameStrategy()

@pytest.fixture
def search_by_type_strategy():
    return SearchByTypeStrategy()


@patch('search.search_by_name.os.walk')
def test_search_file_found(mock_os_walk, search_by_name_strategy):
    mock_os_walk.return_value = [
        ('/mocked/dir', ['subdir'], ['testfile.txt', 'otherfile.txt']),
        ('/mocked/dir/subdir', [], ['anotherfile.txt'])
    ]

    with patch('search.files_infos.FileInfos') as mock_file_infos:
        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.return_value = {
            'filename': 'testfile.txt',
            'path': '/mocked/dir/testfile.txt',
            'type': 'Fichier',
            'abstract': ''
        }
        results = search_by_name_strategy.search(['/mocked/dir'], 'testfile')

        assert len(results) == 1
        assert results[0]['filename'] == 'testfile.txt'
        assert os.path.normpath(results[0]['path']) == os.path.normpath('/mocked/dir/testfile.txt')

@patch('search.search_by_name.os.walk')
def test_search_file_not_found(mock_os_walk, search_by_name_strategy):
    mock_os_walk.return_value = [
        ('/mocked/dir', ['subdir'], ['otherfile.txt']),
        ('/mocked/dir/subdir', [], ['anotherfile.txt'])
    ]

    results = search_by_name_strategy.search(['/mocked/dir'], 'testfile')
    assert len(results) == 0

@patch('search.search_by_name.os.walk')
def test_search_directory_not_found(mock_os_walk, search_by_name_strategy):
    mock_os_walk.return_value =  [
        ('/mocked/dir', ['testfile'], ['otherfile.txt']),
        ('/mocked/dir/testfile', [], ['anotherfile.txt'])
    ]

    with patch("search.files_infos.FileInfos") as mock_file_infos:
        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.return_value = {
            'filename': 'testfile',
            'path': '/mocked/dir/testfile',
            'type': 'Fichier',
            'abstract': ''
        }

        results = search_by_name_strategy.search(['/mocked/dir'], 'testfile')

        assert len(results) == 1
        assert results[0]['filename'] == 'testfile'
        assert os.path.normpath(results[0]['path']) == os.path.normpath('/mocked/dir/testfile')


@patch('search.search_by_type.glob.glob')
def test_search_file_found_with_pattern(mock_glob, search_by_type_strategy):
    mock_glob.return_value = [
        "/mocked/dir/main.cpp",
        "/mocked/dir/note.txt",
        "/mocked/dir/index.html",
        "/mocked/dir/cours.js",
        "/mocked/dir/textes.cpp"
    ]

    with patch('search.files_infos.FileInfos') as mock_file_infos:
        def mock_to_dict():
            return {
                'filename': os.path.basename(mock_file_infos.return_value.path),
                'path': mock_file_infos.return_value.path,
                'type': 'Fichier',
                'abstract': ''
            }

        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.side_effect = mock_to_dict

        results = search_by_type_strategy.search(['/mocked/dir'], 'txt')

        assert len(results) == 1
        assert results[0]['filename'] == 'note.txt'
        assert results[0]['path'] == '/mocked/dir/note.txt'
        assert results[0]['type'] == 'Fichier'
        assert results[0]['abstract'] == ''


if __name__ == '__main__':
    pytest.main()
