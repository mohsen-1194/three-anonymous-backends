import random
import string

import requests

URLS = [
    "http://django:8000",
    "http://flask:8001",
    "http://fastapi:8002",
]


def test_dif_input_same_output(urls):
    for i in range(10):
        characters = string.ascii_letters
        random_string = "".join(
            random.choice(characters) for _ in range(random.randint(1, 20))
        )

        data = {f"{random_string}": f"{random_string}"}
        q_params = {"name": f"{random_string}"}
        cus_headers = {"x-custom-cookie": f"{random_string}"}

        all_resp = []
        for i in range(3):
            resp = requests.post(
                urls[i], params=q_params, headers=cus_headers, json=data
            )
            response = []
            response.append(resp.headers)
            response.append(resp.json())
            all_resp.append(response)

        for item in all_resp:
            del item[0]["Date"]

        if (
            (all_resp[0] == all_resp[1])
            and (all_resp[0] == all_resp[2])
            and (all_resp[1] == all_resp[2])
        ):
            print("Same Output")
        else:
            print("Not the same")


def main():
    test_dif_input_same_output(URLS)


if __name__ == "__main__":
    main()
