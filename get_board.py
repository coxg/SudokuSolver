from json import JSONDecodeError

import requests
import json


def get_board() -> [list[list[int]], str]:
    response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
    try:
        response_dict = json.loads(response.text)
    except JSONDecodeError:
        print(response.text)
    grid = response_dict["newboard"]["grids"][0]
    return grid["value"], grid["difficulty"]