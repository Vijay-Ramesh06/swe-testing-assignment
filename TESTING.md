# TESTING.md

## Testing Strategy

The Quick-Calc project follows a structured testing strategy to ensure the correctness and reliability of the calculator functionality. The main focus of testing was to validate the correctness of arithmetic operations and verify that different parts of the application interact correctly.

The testing process was divided into **unit testing** and **integration testing**. Unit tests focus on verifying the behavior of individual functions within the calculator logic, while integration tests verify that the calculator interface interacts properly with the underlying calculation logic.

### What Was Tested

The following components were tested:

* Core arithmetic operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Edge cases such as:

  * Division by zero
  * Negative numbers
  * Decimal numbers
  * Large numbers
* Interaction between the CLI interface and the calculator logic
* Reset behavior using the clear function

### What Was Not Tested

The following aspects were intentionally not tested in this project:

* Graphical user interface behavior (since the project focuses on logic rather than UI)
* Performance or load testing
* Security testing
* Stress testing

These were excluded because the project scope focuses primarily on **functional correctness and testing methodology**.

---

# Testing Pyramid

The testing structure of this project follows the **Testing Pyramid principle**, which suggests that most tests should be unit tests, with fewer integration tests and even fewer system-level tests.

In this project:

* **Unit Tests (Majority)**
  These tests verify individual calculator methods such as addition, subtraction, multiplication, and division. Unit tests form the base of the testing pyramid because they are fast, simple, and isolate specific pieces of functionality.

* **Integration Tests (Smaller Portion)**
  Integration tests verify that the CLI interface correctly communicates with the calculator logic. For example, they simulate a user performing a calculation through the interface.

Because the application is small, system-level or end-to-end tests were not required.

---

# Black-Box vs White-Box Testing

Both **white-box testing** and **black-box testing** approaches were used in this project.

### White-Box Testing

Unit tests use a **white-box testing approach**, where the internal structure of the program is known and tested directly. For example, individual methods such as `add()`, `subtract()`, `multiply()`, and `divide()` are tested independently. This allows verification that the internal logic works correctly for different inputs.

### Black-Box Testing

Integration tests follow a **black-box testing approach** because they focus on the input and output behavior of the system without examining the internal implementation. For example, a user interaction such as entering "5 + 3" and expecting the result "8" is tested without directly inspecting how the calculation is performed internally.

---

# Functional vs Non-Functional Testing

The tests implemented in this project focus primarily on **functional testing**.

### Functional Testing

Functional testing verifies that the calculator performs the required operations correctly according to the specification. The following functionality was tested:

* Correct arithmetic results
* Handling of division by zero
* Handling of different numeric values (negative numbers, decimals, large numbers)
* Correct interaction between components

### Non-Functional Testing

Non-functional aspects such as performance, usability, scalability, and security were not included in the test suite. These aspects were outside the scope of this assignment and would normally be tested in larger production systems.

---

# Regression Testing

The test suite can also serve as a **regression testing tool** for future development. Regression testing ensures that newly added features or code changes do not break existing functionality.

Whenever modifications are made to the calculator logic or interface, the full test suite can be executed using:

pytest

If any previously working functionality breaks, the failing tests will quickly identify the issue. This helps maintain software stability as the project evolves.

---

# Test Results Summary

The table below summarizes the implemented tests and their results.

| Test Name             | Type        | Description                           | Result |
| --------------------- | ----------- | ------------------------------------- | ------ |
| test_addition         | Unit        | Tests addition of two numbers         | Pass   |
| test_subtraction      | Unit        | Tests subtraction operation           | Pass   |
| test_multiplication   | Unit        | Tests multiplication operation        | Pass   |
| test_division         | Unit        | Tests division operation              | Pass   |
| test_negative_numbers | Unit        | Tests operations with negative values | Pass   |
| test_decimal_numbers  | Unit        | Tests operations with decimal values  | Pass   |
| test_large_numbers    | Unit        | Tests operations with large numbers   | Pass   |
| test_division_by_zero | Unit        | Ensures division by zero is handled   | Pass   |
| test_full_calculation | Integration | Simulates a full calculation via CLI  | Pass   |
| test_clear_function   | Integration | Verifies reset functionality          | Pass   |

---

# Conclusion

The implemented test suite ensures that the core functionality of the Quick-Calc application works correctly and consistently. By combining unit tests and integration tests, the project demonstrates practical application of software testing principles discussed in the lecture.

The testing strategy also reflects best practices such as the Testing Pyramid, separation of test types, and the ability to support regression testing in future versions of the application.
