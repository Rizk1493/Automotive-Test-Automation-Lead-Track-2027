# Week 01 Plan - Python Foundations

## Dates

21 August 2026 - 27 August 2026

## Total Study Time

27 Hours

## Main Goal

Build reliable Python foundations for test automation.

By the end of Week 01, I should be able to:

- Write basic Python programs without step-by-step help
- Understand and use Python core data types
- Work confidently with strings and collections
- Use conditions and loops correctly
- Write reusable functions
- Read and debug basic Python code
- Apply Python to simple automotive validation problems
- Explain Python fundamentals in a technical interview

---

# Friday - 21 August
## Total: 8 Hours

## Session 1 - 4 Hours
### Python Core Foundations

Topics:

- How Python executes code
- Variables
- Naming conventions
- int
- float
- bool
- str
- None
- type()
- isinstance()
- Type conversion
- Basic operators
- Comparison operators
- Boolean operators
- Input and output
- f-strings

Hands-on:

- Small coding exercises after every topic
- ECU information variables
- Voltage and temperature calculations
- PASS / FAIL signal checks

Interview focus:

- Dynamic typing
- Mutable vs immutable introduction
- Difference between = and ==
- Difference between int and float
- Truthy and falsy values

---

## Session 2 - 4 Hours
### Strings + Indexing + Slicing

Topics:

- String creation
- Indexing
- Negative indexing
- Slicing
- step
- Common string methods
- split()
- join()
- strip()
- replace()
- find()
- startswith()
- endswith()
- String immutability

Hands-on:

- Parse ECU identifiers
- Extract parts of CAN-style messages
- Clean test log strings
- Validate diagnostic response text

Automotive Exercise:

Create a small program that receives an ECU test-result string and extracts:

- ECU name
- Test ID
- Test status

---

# Saturday - 22 August
## Total: 4 Hours

### Python Collections

Topics:

- List
- Tuple
- Set
- Dictionary

For each collection:

- Creation
- Access
- Update
- Delete
- Iteration
- Important methods
- When to use it
- Mutable vs immutable
- Duplicate behavior

Hands-on:

- Store test cases
- Store DTC codes
- Remove duplicate failures
- Map DTC IDs to descriptions
- Store ECU signal values

Interview focus:

Explain when to use:

List vs Tuple  
List vs Set  
Dictionary vs List

---

# Sunday - 23 August
## Total: 3 Hours

### Conditions and Boolean Logic

Topics:

- if
- elif
- else
- Nested conditions
- and
- or
- not
- Membership operators
- Identity operators
- Conditional expressions

Automotive Exercise:

Create a signal validator that evaluates:

- Battery voltage
- Engine temperature
- Communication status

and returns an overall test result.

---

# Monday - 24 August
## Total: 3 Hours

### Loops

Topics:

- for
- while
- range()
- enumerate()
- break
- continue
- Nested loops
- Looping over lists
- Looping over dictionaries

Automotive Exercise:

Process multiple ECU test results and calculate:

- Total tests
- Passed
- Failed
- Pass percentage

---

# Tuesday - 25 August
## Total: 3 Hours

### Comprehensions + Practical Data Processing

Topics:

- List comprehensions
- Conditional comprehensions
- Dictionary comprehensions
- Set comprehensions

Hands-on:

Process a test-result dataset and:

- Extract failed tests
- Extract unique DTCs
- Build test-result dictionaries

Focus:

Readable code first.  
Short code is not automatically better code.

---

# Wednesday - 26 August
## Total: 3 Hours

### Functions

Topics:

- Function definition
- Parameters
- Arguments
- return
- Default parameters
- Keyword arguments
- Scope
- Local vs global variables
- Basic type hints
- Docstrings

Automotive Exercise:

Build reusable functions for:

- Signal validation
- DTC lookup
- Test result calculation
- Test summary generation

Interview focus:

- Parameter vs argument
- print vs return
- Local vs global scope
- Why functions improve test automation

---

# Thursday - 27 August
## Total: 3 Hours

### Week 01 Assessment

Part 1:
Python fundamentals review

Part 2:
Coding problems without step-by-step help

Part 3:
Automotive mini task

Build a simple:

ECU Validation Result Processor

The program should:

- Store test results
- Detect failures
- Calculate pass percentage
- Identify failed test IDs
- Generate a readable summary

Part 4:
Technical interview questions

Part 5:
Explain selected code in English

Part 6:
Review mistakes and update Progress Tracker

---

# Week 01 Required Outputs

## Code

- Fundamentals exercises
- String exercises
- Collections exercises
- Conditions exercises
- Loop exercises
- Functions exercises
- ECU Validation Result Processor

## Notes

Python Foundations Notes

## Interview

Python Fundamentals Q&A

## Test Documentation

Simple ECU validation test cases

## GitHub

Regular commits throughout the week

## Assessment

Final coding assessment

## Mock Interview

Python fundamentals technical interview

---

# Week 01 Success Criteria

Week 01 is complete only if I can:

1. Write basic Python code without copying solutions.
2. Explain the code I write.
3. Select appropriate basic data structures.
4. Solve basic programming problems.
5. Apply Python to automotive validation examples.
6. Answer core Python interview questions.
7. Complete the final ECU validation task.

Weak topics will be carried into Week 02 instead of being marked complete artificially.
