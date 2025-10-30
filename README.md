# SaveJSON

SaveJSON is a Python utility class for easily saving and loading JSON files. Designed to offer robust logging, error handling, and flexible directory support, it helps manage persistent data in your projects.

## Features

- Save any Python object to a JSON file with clear logs.
- Load data from JSON files safely and efficiently.
- Configure the storage directory for flexible setups.
- Seamless integration with Python logging for detailed tracing.
- Handles errors gracefully and logs informative messages.

## Installation

Clone the repository
git clone https://github.com/Vin8th/SaveJSON.git


Or simply copy `SaveJSON.py` into your project folder.

## Usage

from SaveJSON import SaveJSON
import logging

logger = logging.getLogger("jsonLogger")
savejson = SaveJSON(logger, base_dir="your/data/path")

data = {"name": "Test", "age": 25}
savejson.save("test.json", data)

loaded = savejson.load("test.json")
print(loaded)



## API Reference

### SaveJSON class

- `__init__(self, log: Logger, base_dir: str)`
    - Initialize with logger and data directory path.

- `save(filename: str, obj: dict)`
    - Save a dictionary or object to a JSON file.

- `load(filename: str) -> dict`
    - Load data from a JSON file.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

MIT License

## Contact

Maintainer: Vin8th  
Email: bvineeth96@gmail.com
