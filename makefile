lint:
	poetry run ruff check .
mypy:
	poetry run mypy .
test:
	poetry run pytest tests/