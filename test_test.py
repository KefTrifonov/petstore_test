import requests

import pytest


class TestPet:

    def test_post_new_pet(self):

        base_url = 'https://petstore.swagger.io/v2/pet/'

        post_pet_body = {
            "id": 2565684315,
            "category": {
                "id": 0,
                "name": "Cats"
            },
            "name": "Testing name",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        post_pet = requests.post(base_url, json=post_pet_body)
        assert post_pet.status_code == 200
        assert post_pet.json()["name"] == 'Testing name'

    def test_get_pet(self):

        base_url = 'https://petstore.swagger.io/v2/pet/'
        pet_id = 2565684315
        get_pet = requests.get(f"{base_url}+{pet_id}")
        assert get_pet.status_code == 200

    def test_put_pet(self):

        put_pet_body = {
            "id": 2565684315,
            "category": {
                "id": 0,
                "name": "Cats"
            },
            "name": "Changed name",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        base_url = 'https://petstore.swagger.io/v2/pet/'
        put_pet_id = 2565684315
        put_pet = requests.put(f"{base_url}+{put_pet_id}", json=put_pet_body)
        assert put_pet.status_code == 200
        assert put_pet.json()["name"] == "Changed name"
