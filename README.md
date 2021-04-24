![GitHub](https://img.shields.io/github/license/jreig/cnf-encoder)

# cnfencoder

**cnfencoder** is a Python library for dealing with propositional formulas and transform them into CNF formulas. Aditionaly, the package contains data structures to manage them and tools for encoding to and from DIMACS file format.

Transformation to CNF is done using Tseytin transformation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install it.

```bash
pip install cnfencoder
```

## Usage

```python
import cnfencoder
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### Run tests

```bash
$ nosetests
```

## License
The package is licensed under [MIT](LICENSE) license