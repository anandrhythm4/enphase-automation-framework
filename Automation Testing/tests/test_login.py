from utils.api_helper import get, post
import pytest,json

def test_get_posts(config, logger):
    endpoint = config["endpoints"]["posts"]
    response = get(endpoint)
    logger.info(f"GET {endpoint} - Status: {response.status_code}")

    try:
        data = response.json()
        pretty_json = json.dumps(data, indent=2)
        logger.info(f"Response JSON:\n{pretty_json}")
    except Exception as e:
        logger.error(f"Failed to parse JSON response: {e}")
        logger.error(f"Raw response text: {response.text}")

    assert response.status_code == 200

@pytest.mark.parametrize("payload", [
    {"title": "foo", "body": "bar", "userId": 1},
    {"title": "another", "body": "test", "userId": 2}
])
def test_create_post(config, logger, payload):
    endpoint = config["endpoints"]["posts"]
    response = post(endpoint, payload)
    logger.info(f"POST {endpoint} - Payload: {payload}")
    assert response.status_code == 201