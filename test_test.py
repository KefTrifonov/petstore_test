import requests


class TestPet:

    def __init__(self):
        pass

    def post_new_pet(self):

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

        print("Status code: " + str(post_pet.status_code))
        if post_pet.status_code == 200:
            print(f"Created pet: {post_pet.json()}")

        else:
            print(f"Wrong credentials {post_pet.json()}")

        post_pet_id = post_pet_body["id"]

        post_pet_get = requests.get(f"{base_url}+{post_pet_id}")

        print(post_pet_get.status_code)
        print(post_pet_get.json())

    def test_get_pet(self):

        base_url = 'https://petstore.swagger.io/v2/pet/'
        pet_id = 90909
        result = requests.get(f"{base_url}+{pet_id}")
        print("Status code: " + str(result.status_code))
        if result.status_code == 200:
            print(f"Found pet: {result.json()}")

        else:
            print(f"Pet doesn't exists {result.json()}")

        result.encoding = 'utf-8'
        check = result.json()
        check_info = check.get('name')
        assert check_info == 'Andrey'
        print("Passed")


create_pet = TestPet()
get_pet = TestPet()
create_pet.post_new_pet()
get_pet.test_get_pet()
