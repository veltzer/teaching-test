# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml:9-14` - `ruff` and `mypy` only cover `src_dirs = ["tests"]`, so `add.py` (the module the whole demo is about) is never linted or type-checked; add `src_files = ["add.py"]` to both processors.
- `Jenkinsfile:6` - runs bare `python -m pytest` with no step that creates the environment; `pytest` is only declared in the `dev` dependency group (`pyproject.toml:11-15`), so on a clean Jenkins agent the stage fails unless pytest happens to be installed globally. Add a setup step (`uv sync` and run inside `.venv`) before the test stage.

## Low

- `rsconstruct.toml:1` - the repo carries the shared `.yamllint.yaml` and YAML files under `.github/`, but no `[processor.yamllint]` is configured, so the config is unused; add `[processor.yamllint]` with `src_dirs = [".github"]` like the other repos that lint YAML.
- `.github/dependabot.yml:1` - generated from `tera.templates/.github/dependabot.yml.tera`, but `rsconstruct.toml` has no `[processor.tera]`, so the output is not regenerated (it already differs from the template's blank-line layout); add the tera processor or render it and commit the result.
