from get_board import get_board
from solver import solve, is_solved

def gather_metrics(n: int) -> None:
    metrics = {
        "Easy": [],
        "Medium": [],
        "Hard": []
    }

    for _ in range(n):
        board, difficulty = get_board()
        solve(board)
        metrics[difficulty].append(is_solved(board))

        print(".", end="")

    print()

    for _difficulty in ("Easy", "Medium", "Hard"):
        success = sum(metrics[_difficulty])
        attempts = len(metrics[_difficulty])
        if not attempts:
            continue

        print(f"{_difficulty}: {success} / {attempts} = {success * 100 // attempts}%")


if __name__ == "__main__":
    gather_metrics(100)