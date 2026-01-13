# Makefile for Regression Test Suite

.PHONY: help install test test-smoke test-regression test-parallel test-headless clean report

# Default target
help:
	@echo "Available targets:"
	@echo "  install          - Install dependencies"
	@echo "  setup            - Setup environment (copy .env.example to .env)"
	@echo "  test             - Run all tests"
	@echo "  test-smoke       - Run smoke tests only"
	@echo "  test-regression  - Run regression tests only"
	@echo "  test-parallel    - Run tests in parallel"
	@echo "  test-headless    - Run tests in headless mode"
	@echo "  test-firefox     - Run tests in Firefox"
	@echo "  test-edge        - Run tests in Edge"
	@echo "  report           - Generate HTML report"
	@echo "  clean            - Clean up generated files"

# Install dependencies
install:
	pip install -r requirements.txt

# Setup environment
setup:
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo ".env file created. Please update with your settings."; \
	else \
		echo ".env file already exists."; \
	fi

# Run all tests
test:
	pytest -v

# Run smoke tests
test-smoke:
	pytest -v -m smoke

# Run regression tests
test-regression:
	pytest -v -m regression

# Run tests in parallel (4 workers)
test-parallel:
	pytest -v -n 4

# Run tests in headless mode
test-headless:
	HEADLESS=true pytest -v

# Run tests in Firefox
test-firefox:
	BROWSER=firefox pytest -v

# Run tests in Edge
test-edge:
	BROWSER=edge pytest -v

# Generate HTML report
report:
	pytest -v --html=reports/report.html --self-contained-html

# Clean up generated files
clean:
	rm -rf reports/* screenshots/* .pytest_cache __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
