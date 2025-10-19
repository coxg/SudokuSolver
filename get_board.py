import requests
import json

def get_board() -> [list[list[int]], str]:
    attempts = 10
    for attempt in range(attempts):
        try:
            return _get_board()
        except:
            pass
    raise RuntimeError(f"{attempts} attempts exceeded")


def _get_board() -> [list[list[int]], str]:
    response = requests.get("https://sudoku-api.vercel.app/api/dosuku")
    response_dict = json.loads(response.text)
    grid = response_dict["newboard"]["grids"][0]
    return grid["value"], grid["difficulty"]