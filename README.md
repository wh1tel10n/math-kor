# Math Kor

## install
```sh
pip install --index-url https://test.pypi.org/simple/ math-kor
```

## Usage

```python
>>> from math_kor.basic import 더하기
>>> 더하기(1,2)
3
```

## Development

1. Setup development environment

    ```sh
    cd ~/PROJECT/PATH
    virtualenv -p python3 .venv
    source .venv/bin/activate
    pip install -r requirements
    ```

2. Use doctest
    ```sh
    python -m doctest math_kor/basic.py
    ```

3. Run unittest
    ```sh
    pytest
    ```
    > ```sh
    > python -m unittest discover tests -p test*.py
    > ```

