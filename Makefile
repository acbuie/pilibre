format:
	ruff --select "I001" --fix src/
	black src/

test:
	pytest -ra tests/

test-report:
	pytest -ra --cov-report xml:cov.xml --cov:src/ tests/

test-report-terminal:
	pytest -ra --cov-report term-missing --cov=src/ tests/

lint:
	ruff src/ --quiet

lint-verbose:
	ruff src/

typecheck:
	mypy src/

typecheck-report:
	mypy src/ --html-report mypy_report
