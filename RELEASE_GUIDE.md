# Release Guide

This package follows the GenesisAeon ecosystem release process.

## Versioning

We use [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **MAJOR** — breaking changes to the public API (e.g. `entropy_wave_to_audio`,
  `utac_to_midi`, the `soni` CLI).
- **MINOR** — new features, backwards-compatible.
- **PATCH** — bug fixes, documentation, dependency bumps.

## Release types

| Tag pattern | Channel | Where it publishes |
|---|---|---|
| `vX.Y.Z` | Production | PyPI, GitHub Release, Zenodo (if integration enabled) |
| `vX.Y.Z-rc.N`, `-alpha.N`, `-beta.N` | Canary | GitHub pre-release |

## How to cut a release

1. Ensure `CHANGELOG.md` has an entry for the new version under
   `## [X.Y.Z]`.
2. Ensure `pyproject.toml`'s `[project].version` matches.
3. Ensure `.zenodo.json`'s `"version"` field matches.
4. Ensure `CITATION.cff`'s `version` field matches.
5. Commit these changes (if any) to `main`.
6. Tag: `git tag vX.Y.Z && git push origin vX.Y.Z`.
7. The `.github/workflows/release.yml` workflow builds, tests, and
   publishes automatically.
8. For production releases, if Zenodo-GitHub integration is enabled for
   this repo, a new Zenodo DOI version is minted automatically from the
   GitHub Release using `.zenodo.json` metadata.

## Dependency pins within the GenesisAeon ecosystem

`sonification` depends on the `[stack]` optional extra
(`mandala-visualizer`, `utac-core`, `sigillin`, `fieldtheory`,
`cosmic-moment`, `medium-modulation`, `entropy-governance`,
`entropy-table`, `implosive-genesis`). Pin these with `>=` lower bounds
matching the minimum version that provides the API this package relies
on. Do not pin exact versions (`==`) for ecosystem dependencies.
