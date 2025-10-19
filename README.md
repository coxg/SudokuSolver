# Sudoku Solver

A Python-based Sudoku solver with a FastAPI backend for generating and solving Sudoku puzzles.

## Features

- Automated Sudoku puzzle solving using constraint-based logic
- REST API for puzzle generation and solving
- Support for standard 9x9 Sudoku grids

## Project Structure

- `solver.py` - Core Sudoku solving algorithm
- `api.py` - FastAPI REST API endpoints
- `get_board.py` - Puzzle generation functionality
- `tests.py` - Unit tests
- `gather_metrics.py` - Performance metrics collection

## API Endpoints

### GET /get_board
Generates a new Sudoku puzzle.

**Response:**
```json
{
  "board": [[...], [...]],
  "difficulty": "easy|medium|hard"
}
```

### POST /solve_board
Solves a provided Sudoku puzzle.

**Request:**
```json
{
  "board": [[...], [...]]
}
```

**Response:**
```json
{
  "solved_board": [[...], [...]],
  "success": true
}
```

## Installation

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn pydantic
```

## Usage

### Running the API

```bash
uvicorn api:app --reload
```

The API will be available at `http://localhost:8000`

### Using the Solver Directly

```python
from solver import solve, is_solved

# Define your Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    # ... rest of board
]

solve(board)
print(is_solved(board))  # True if solved
```

## Running Tests

```bash
python tests.py
```
