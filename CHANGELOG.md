# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-06-28
### Added
- Initial v1.0.0 release as part of the GenesisAeon ecosystem-wide 1.0.0
  milestone.
- Standardized release tooling: `RELEASE_GUIDE.md`, `CONTRIBUTING.md`,
  issue/PR templates.

### Changed
- Project metadata (`pyproject.toml`, `.zenodo.json`, `CITATION.cff`)
  normalized: version bumped to `1.0.0`, GenesisAeon-ecosystem dependency
  pins updated to their real released floors (`entropy-table>=2.0.0`,
  `implosive-genesis>=1.0.0`, and others in the `[stack]` extra).
- License clarified as dual: GPLv3-or-later for code, CC BY 4.0 for
  documentation, resolving a prior inconsistency where the `LICENSE` file
  said MIT while the README/`.zenodo.json` already stated GPLv3 — the
  repository now consistently uses the latter as originally documented.
