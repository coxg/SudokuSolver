from fastapi import FastAPI
from get_board import get_board
from solver import solve, is_solved
from pydantic import BaseModel

app = FastAPI()


@app.get("/get_board")
async def _get_board():
    board, difficulty = get_board()
    return {
        "board": board,
        "difficulty": difficulty
    }

class BoardRequest(BaseModel):
    board: list[list[int]]


@app.post("/solve_board")
async def solve_board(request: BoardRequest):
  solve(request.board)
  return {
      "solved_board": request.board,
      "success": is_solved(request.board)
  }
