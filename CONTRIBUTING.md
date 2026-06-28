# Contributing

Thanks for your interest in contributing to `sonification`!

## Getting started

1. Fork and clone the repository.
2. Create a virtual environment: `python -m venv .venv && source .venv/bin/activate`
   (or `.venv\Scripts\activate` on Windows).
3. Install in editable mode with dev dependencies: `pip install -e ".[dev]"`.
4. Run the test suite: `pytest`.

## Code style

- Format and lint with `ruff check src tests` / `ruff format`.
- Type-check with `mypy src` (strict mode is enabled).
- Keep functions documented with docstrings.

## Pull requests

- One logical change per PR.
- Add or update tests for any behavioral change.
- Update `CHANGELOG.md` under an `## [Unreleased]` section.
- Fill out the PR template (`.github/PULL_REQUEST_TEMPLATE.md`).

## Reporting issues

Please use the issue templates in `.github/ISSUE_TEMPLATE/` — they help us
triage bug reports vs. feature requests quickly.

## Licensing

Code contributions are licensed under GPLv3-or-later; documentation
contributions are licensed under CC BY 4.0 (see `LICENSE` and
`LICENSE-DOCS`). By submitting a contribution you agree to license it
under these terms.
