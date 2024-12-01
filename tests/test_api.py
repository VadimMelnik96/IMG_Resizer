import uuid

import pytest


@pytest.mark.asyncio
async def test_uploads(client) -> None:
    """Тест входной точки загрузки изображения"""
    image_data = b"fake-image-content"
    files = {'file': ('test.jpg', image_data, 'image/jpeg')}
    response = client.post(
        "/upload", files=files
    )
    assert response.status_code == 200
    assert 'task_id' in response.json() and isinstance(response.json()['task_id'], str)



@pytest.mark.asyncio
async def test_status(client) -> None:
    """Тест входной точки получения статуса изображения"""
    response = client.get(
        f"/status/{uuid.uuid4()}",
    )
    assert response.status_code == 200
    assert response.json().get('status') == "SUCCESS"
    assert response.json().get('image_url')
