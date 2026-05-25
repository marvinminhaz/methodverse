# Methodverse
A fast, lightweight reference engine for Python built-in methods. Get quick
explanations and examples without digging through official documentation.

## Installation
pip install methodverse

## Usage
from methodverse import explain, enlist

explain('list', 'append')   # prints description + example
enlist('dict')              # prints all available dict methods

## Structure
```
methodverse/
├── methodverse/
│   ├── __init__.py
│   └── core.py
├── README.md
├── LICENSE
└── pyproject.toml
```