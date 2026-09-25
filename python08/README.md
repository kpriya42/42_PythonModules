
## Poetry
Poetry can be used with a virtual environment, but normally you do not need to manually create one because Poetry manages virtual environments itself.

		poetry install
		poetry run python <name_of_py_file>
		poetry env info

## Common command comparison

| Task                      | `pip`                             | `poetry`                    | `uv`                    |
| ------------------------- | --------------------------------- | --------------------------- | ----------------------- |
| Create project            | Manual                            | `poetry new app`            | `uv init`               |
| Create virtual env        | `python -m venv .venv`            | Automatic                   | `uv venv`               |
| Add package               | `pip install requests`            | `poetry add requests`       | `uv add requests`       |
| Run script                | `python main.py`                  | `poetry run python main.py` | `uv run python main.py` |
| Install from lock/project | `pip install -r requirements.txt` | `poetry install`            | `uv sync`               |
| Lock dependencies         | Needs extra tools                 | `poetry lock`               | `uv lock`               |



## Exercise 3 priority calculation:

```
Shell environment variables (highest priority)
      │
      ▼
.env values
      │
      ▼
program defaults (lowest priority)
```

load_dotenv() behaves approximately like this:

```
for each variable in .env:
    if variable is NOT already in os.environ:
        add it to os.environ
```

```
.env file
   |
   | load_dotenv()
   v
os.environ
   ^
   |
Shell environment variables
```