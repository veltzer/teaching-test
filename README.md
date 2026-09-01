# teaching-test

A minimal Python project used to demonstrate CI pipelines in class.

`add.py` has one function, `tests/` has pytest tests for it, and the
`Jenkinsfile` runs them. The GitHub Actions workflow runs the same tests via
`rsconstruct`.
