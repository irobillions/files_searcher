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

def mock_os_stat(path):
    mock_stat_result = MagicMock()
    mock_stat_result.st_atime = 1609459200  # 2021-01-01 00:00:00
    mock_stat_result.st_mtime = 1609459200  # 2021-01-01 00:00:00
    mock_stat_result.st_ctime = 1609459200  # 2021-01-01 00:00:00
    return mock_stat_result

def mock_os_path_isdir(path):
    # Simuler isdir pour retourner False pour les fichiers et True pour les répertoires
    if path in ['/mocked/dir', '/mocked/dir/subdir']:
        return True
    return False

def mock_os_path_exists(path):
    # Simuler exists pour retourner True pour les chemins fictifs
    return path in [
        '/mocked/dir',
        '/mocked/dir/subdir',
        '/mocked/dir/testfile.txt',
        '/mocked/dir/otherfile.txt',
        '/mocked/dir/subdir/anotherfile.txt',
        '/mocked/dir/testfile',
        '/mocked/dir/note.txt'
    ]

@patch('search.search_by_name.os.walk')
@patch('search.files_infos.os.stat', side_effect=mock_os_stat)
@patch('search.files_infos.os.path.isdir', side_effect=mock_os_path_isdir)
@patch('search.files_infos.os.path.exists', side_effect=mock_os_path_exists)
def test_search_file_found(mock_os_exists, mock_os_isdir, mock_os_stat, mock_os_walk, search_by_name_strategy):
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
            'abstract': '',
            "access_time": '2021-01-01 00:00:00',
            "creation_time": '2021-01-01 00:00:00',
            "modification_time": '2021-01-01 00:00:00'
        }
        results = search_by_name_strategy.search(['/mocked/dir'], 'testfile')

        assert len(results) == 1
        assert results[0]['filename'] == 'testfile.txt'
        assert os.path.normpath(results[0]['path']) == os.path.normpath('/mocked/dir/testfile.txt')

@patch('search.search_by_name.os.walk')
@patch('search.files_infos.os.stat', side_effect=mock_os_stat)
@patch('search.files_infos.os.path.isdir', side_effect=mock_os_path_isdir)
@patch('search.files_infos.os.path.exists', side_effect=mock_os_path_exists)
def test_search_directory_not_found(mock_os_exists, mock_os_isdir, mock_os_stat, mock_os_walk, search_by_name_strategy):
    mock_os_walk.return_value = [
        ('/mocked/dir', ['testfile'], ['otherfile.txt']),
        ('/mocked/dir/testfile', [], ['anotherfile.txt'])
    ]

    with patch("search.files_infos.FileInfos") as mock_file_infos:
        mock_instance = mock_file_infos.return_value
        mock_instance.to_dict.return_value = {
            'filename': 'testfile',
            'path': '/mocked/dir/testfile',
            'type': 'Fichier',
            'abstract': '',
            "access_time": '2021-01-01 00:00:00',
            "creation_time": '2021-01-01 00:00:00',
            "modification_time": '2021-01-01 00:00:00'
        }

        results = search_by_name_strategy.search(['/mocked/dir'], 'testfile')

        assert len(results) == 1
        assert results[0]['filename'] == 'testfile'
        assert os.path.normpath(results[0]['path']) == os.path.normpath('/mocked/dir/testfile')

@patch('search.search_by_type.glob.glob')
@patch('search.files_infos.os.stat', side_effect=mock_os_stat)
@patch('search.files_infos.os.path.isdir', side_effect=mock_os_path_isdir)
@patch('search.files_infos.os.path.exists', side_effect=mock_os_path_exists)
def test_search_file_found_with_pattern(mock_os_exists, mock_os_isdir, mock_os_stat, mock_glob, search_by_type_strategy):
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
                'abstract': '',
                "access_time": '2021-01-01 00:00:00',
                "creation_time": '2021-01-01 00:00:00',
                "modification_time": '2021-01-01 00:00:00'
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
