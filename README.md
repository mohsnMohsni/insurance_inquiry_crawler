# Insurance inquiry

[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20static%20analysis-flake8-%eb4034b1?style=flat)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

### How to set up project:

install dependencies:
- Production:
    ```bash
    pip install -r requirements/production.txt
    ```
- Development:
    ```bash
    pip install -r requirements/local.txt
    ```

setup commands:

```bash
./scripts/setup
```

### How to run project:
```bash
start
```

### examples:
```bash
curl -X GET "http://localhost:9080/crawl.json?spider_name=sandbox&national_code=12313123"
```
