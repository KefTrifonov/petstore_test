import requests

import pytest

import random


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

    def test_get_pet_not_exist(self):

        base_url = 'https://petstore.swagger.io/v2/pet/'
        pet_id = 0000000
        get_pet = requests.get(f"{base_url}+{pet_id}")
        assert get_pet.status_code == 404

    def test_update_pet(self):

        base_url = 'https://petstore.swagger.io/v2/pet/'
        put_pet_body = {
          "id": 2565684315,
          "category": {
            "id": 0,
            "name": "string"
          },
          "name": "John",
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
        put_pet = requests.put(f"{base_url}", json=put_pet_body)
        assert put_pet.status_code == 200
        assert put_pet.json()["name"] == "John"

    def test_delete_pet(self):
        base_url = 'https://petstore.swagger.io/v2/pet/'
        delete_pet_id = 2565684315
        delete_pet = requests.delete(f"{base_url}+{delete_pet_id}")
        assert delete_pet.status_code == 200

    def test_delete_pet_not_exist(self):
        base_url = 'https://petstore.swagger.io/v2/pet/'
        delete_pet_id = 00000
        delete_pet = requests.delete(f"{base_url}+{delete_pet_id}")
        assert delete_pet.status_code == 404

    def test_get_pet_by_status(self):
        base_url = 'https://petstore.swagger.io/v2/pet/findByStatus?status='
        parameters = ['available', 'pending', 'sold']
        url_parameter = random.choice(parameters)
        get_pet_by_status = requests.get(f"{base_url}{url_parameter}")
        assert get_pet_by_status.status_code == 200

    def test_get_pet_by_wrong_status(self):
        base_url = 'https://petstore.swagger.io/v2/pet/findByStatus'
        parameters = ['avail', 'peing', 'sld']
        url_parameter = random.choice(parameters)
        get_pet_by_status = requests.get(f"{base_url}{url_parameter}")
        assert get_pet_by_status.status_code == 404
