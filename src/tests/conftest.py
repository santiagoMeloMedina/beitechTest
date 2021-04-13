
import os
import pytest
from configuration.app import app
from configuration.db import db_client

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.fixture(autouse=True)
def setupNoCommitDB():
    db_client.committing = False

