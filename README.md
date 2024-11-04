# Performance Testing Framework

A Python-based performance testing framework that allows users to run performance tests on a specified website, generate detailed reports, and save results in ```.csv```, ```.xlsx```, ```.json``` formats.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Reporting](#reporting)


## Features

- Run performance tests with varying levels of concurrency.
- Generate reports in CSV and JSON formats.
- Automatically create directories for output reports.
- Simple configuration and easy to extend.

## Installation

1. Clone the repository:
   ```git clone https://github.com/lepester/py-perf-framework.git```

2. Create and activate a virtual environment - On Windows:

   ```python -m venv .venv```
 
   ```.venv\Scripts\activate```

3. Create and activate a virtual environment - On macOS/Linux

   ```python -m venv .venv```

   ```source .venv/bin/activate```
4. Install the required dependencies
   ```pip install -r requirements.txt```
5. Go to ```src/config/config.py``` and set target website through variable ```BASE_URL```
## Usage
To run the performance tests, execute the following command in your terminal
   ```python main.py```

### OR
   
Click Play button in ```main.py```

![img_6](https://github.com/user-attachments/assets/995c8694-60f4-4043-aed3-923c1546f1c9)

```create_output_directories():``` This function initializes the necessary directories (e.g., test-output) where test reports and data will be stored. It ensures that the directory structure is ready for storing the results before any tests are executed.

```run_tests():``` This function triggers the main test suite. It performs concurrent requests to the specified URL, collects performance metrics, and generates various report files, including CSV, JSON, Excel, and visualization files. Reports are generated even if some requests fail, allowing for a comprehensive analysis of the performance test results.


## Reporting
Report will be generated at the ending of a test run. It can be found in ```test-output``` directory

![img_5](https://github.com/user-attachments/assets/573741f6-0a78-4766-86a2-63bd536f0a10)

