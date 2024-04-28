import asyncio
import pytest
from fastapi.testclient import TestClient

from week5 import app  # Assuming 'main.py' contains the FastAPI app definition

pytestmark = pytest.mark.asyncio


async def test_create_task():
    async with TestClient(app) as client:
        data = {"duration": 5}

        # Send POST request to create task
        response = await client.post("/task", json=data)
        assert response.status_code == 200

        # Get response data
        response_data = response.json()
        assert "task_id" in response_data

        # Check if task is added to dictionary
        task_id = response_data["task_id"]
        assert response_data[task_id] == "running"

