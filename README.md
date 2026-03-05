# Quick-Calc

Quick-Calc is a simple calculator application developed for the **Advanced Software Engineering** course assignment.
The application performs basic arithmetic operations including addition, subtraction, multiplication, and division. It also includes a clear function to reset the calculator state.

The main goal of this project is to demonstrate **software testing principles**, including **unit testing, integration testing, and version control using Git and GitHub**.

---

# Features

The calculator supports the following operations:

| Operation      | Description                                      | Example    |
| -------------- | ------------------------------------------------ | ---------- |
| Addition       | Adds two numbers                                 | 5 + 3 = 8  |
| Subtraction    | Subtracts one number from another                | 10 - 4 = 6 |
| Multiplication | Multiplies two numbers                           | 6 × 7 = 42 |
| Division       | Divides two numbers and handles division by zero | 8 / 2 = 4  |
| Clear          | Resets the calculator value                      | C → 0      |

---

# Project Structure

```
swe-testing-assignment
│
├── calculator.py
├── cli.py
│
├── tests
│   ├── test_calculator.py
│   └── test_integration.py
│
├── README.md
├── TESTING.md
├── requirements.txt
```

* **calculator.py** – Contains the core calculation logic.
* **cli.py** – Handles the interaction between user input and the calculator logic.
* **tests/** – Contains all unit and integration tests.
* **README.md** – Project documentation.
* **TESTING.md** – Detailed explanation of the testing strategy.

---

# Setup Instructions

Follow these steps to run the project locally.

## 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/swe-testing-assignment.git
cd swe-testing-assignment
```

## 2. Install Dependencies

```
pip install -r requirements.txt
```

This installs the testing framework used in the project.

---

# Running the Application

The calculator logic can be executed through the CLI interface.

Example usage inside Python:

```python
from cli import calculate

result = calculate(5, "+", 3)
print(result)
```

Expected output:

```
8
```

---

# Running the Tests

All tests can be executed using **pytest**.

Run the following command in the project root directory:

```
pytest
```

For detailed output:

```
pytest -v
```

This will execute both **unit tests** and **integration tests**.

---

# Testing Framework Research

## Pytest

Pytest is a modern and widely used Python testing framework designed to make writing and executing tests simple and efficient. It allows developers to write tests using standard Python `assert` statements and requires very little boilerplate code. Pytest also supports advanced features such as fixtures, parameterized testing, and a large ecosystem of plugins.

Another advantage of Pytest is its readability and ease of maintenance. Tests written with Pytest are often shorter and easier to understand compared to traditional testing frameworks. This makes it particularly suitable for small to medium projects where rapid development and clear test structure are important.

## Unittest

Unittest is the built-in testing framework that comes with Python. It is inspired by Java's JUnit framework and follows an object-oriented structure where tests are organized into classes. While it is powerful and stable, it typically requires more boilerplate code compared to Pytest. Developers must define test classes and use specific assertion methods such as `assertEqual()`.

Although Unittest is reliable and widely supported, it can make test files longer and slightly harder to read compared to Pytest.

## Framework Choice

For this project, **Pytest** was selected as the primary testing framework because of its simplicity, readability, and flexibility. The ability to write concise tests using simple assertions makes it ideal for quickly developing and maintaining a comprehensive test suite for the Quick-Calc application.

---

# Version Control

This project follows good version control practices using **Git and GitHub**, including:

* Meaningful commit messages
* Incremental development commits
* Semantic versioning with a release tag

The first stable release of the application is available as:

```
v1.0.0
```

---

# Author

Vijay Ramesh
Riga Technical University
