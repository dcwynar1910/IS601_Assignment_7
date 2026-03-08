import os 
from pathlib import Path
import pytest
import logging
from main import create_directory, is_valid_url, generate_qr_code, setup_logging

def test_create_directory(tmp_path):
    test_path = tmp_path / "testing_qr_dir"
    create_directory(test_path)

    assert test_path.exists()
    assert test_path.is_dir()

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


def test_setup_logging():
    setup_logging()
    assert True



def test_create_directory_except(caplog):
    test_path = Path("/system_folder_test")

    with pytest.raises(Exception):
        create_directory(test_path)

    assert "Failed to create directory" in caplog.text

def test_generate_qr_code_except(caplog):
    test_path = Path("/testing_qr_dir")
    test_url = "https://www.google.com"

    with pytest.raises(Exception):
        generate_qr_code(test_url, test_path, fill_color = "blah")

    assert "An error occurred while generating or saving the QR code" in caplog.text

