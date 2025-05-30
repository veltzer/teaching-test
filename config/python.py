console_scripts = [
]
dev_requires = [
    "pypitools",
]
config_requires = [
    "pyclassifiers",
]
install_requires = [
]
build_requires = [
    "pydmt",
    "pymakehelper",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
