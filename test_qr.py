import os 
from pathlib import Path
import pytest
from main import create_directory, is_valid_url, generate_qr_code

def test_create_directory(tmp_path):
    dir = tmp_path / "testing_qr_dir"
    create_directory(dir)

    assert dir.exists()
    assert dir.is_dir()

def test_is_valid_url():
    test_url = "https://github.com/dcwynar1910"
    assert is_valid_url(test_url) is True

def test_is_NOT_valid_url():
    test_url = "test_bad"
    assert is_valid_url(test_url) is False

def test_generate_qr_code_valid(tmp_path):
    file_path = tmp_path / "testing_qr_dir"
    test_url = "https://www.google.com"

    generate_qr_code(test_url, file_path)

    assert file_path.exists() 
    assert file_path.stat().st_size > 0

def test_generate_qr_code_NOT_valid(tmp_path):
    file_path = tmp_path / "testing_qr_dir"
    test_url = "test_bad"

    generate_qr_code(test_url, file_path)

    assert not file_path.exists()


