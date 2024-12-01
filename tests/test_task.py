from unittest.mock import patch


from src.domain.celery.worker import resize_file


@patch("src.domain.celery.worker.resize_file.run")
def test_mock_task(mock_run):
    """Тест Celery worker"""
    assert resize_file.run("uploads", "resized")
    resize_file.run.assert_called_once_with("uploads", "resized")
