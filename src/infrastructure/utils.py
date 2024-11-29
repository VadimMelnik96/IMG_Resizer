import os

from src.infrastructure.settings.settings import settings


def make_paths(file_name: str) -> tuple[str, str]:
    """Утилита для создания папок"""
    os.makedirs(settings.server_folders.uploads_folder, exist_ok=True)
    os.makedirs(settings.server_folders.resized_folder, exist_ok=True)
    upload_file_path = os.path.join(settings.server_folders.uploads_folder, file_name)
    resized_file_path = os.path.join(settings.server_folders.resized_folder, file_name)
    return upload_file_path, resized_file_path
