# Math Kor

## Development

1. Setup development environment

```
cd ~/PROJECT/PATH
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements
```

2. Use doctest
```
python -m doctest math_kor/basic.py
```

3. Run unittest
```
python -m unittest discover tests -p test*.py
```
