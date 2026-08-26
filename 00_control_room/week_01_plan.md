# Week 01 Plan - Python Foundations Rebuild I

## Dates

**27 August 2026 - 2 September 2026**

## Total Study Time

**45 Hours**

- 9 sessions
- 5 hours/session

---

# Main Goal

Rebuild Python fundamentals specifically around the main current weakness:

> **Turning an Automotive Requirement and a blank screen into structured working code independently.**

This is not a repeat of a beginner Python course and not a syntax-reading week.

Existing knowledge should move quickly when it reaches INITIAL GREEN.

The week focuses on:

```text
Variables + Input/Output
→ Data Types / Conversion
→ Comparisons / Boolean Logic
→ if / elif / else
→ for
→ while
→ Strings
→ Integrated Automotive Problems
```

Lists, dictionaries, functions, and OOP come after this foundation has been independently validated.

---

# Required Learning Method

For each meaningful subtopic:

```text
Explain
→ Complete Automotive Example
→ Edge Cases / Boundary Values
→ Full Independent Automotive Task
→ Review
→ Integration
→ Mastery Check
```

For suitable independent coding tasks Rizk produces:

```text
Analysis
- Input
- Output
- Variables
- Conditions
- Repetition
- Stop condition

Pseudocode
Python Code
Manual Test Cases
Edge Cases / Boundary Values
```

---

# Session 1 - Thursday 27 August
## 5 Hours
### Variables + Input/Output + Data Types + Conversion

Topics:

- Variables and meaningful naming
- `input()`
- `print()`
- `int`
- `float`
- `str`
- `bool`
- Type conversion
- Basic f-strings
- Choosing a type from the Requirement

Automotive examples:

- Battery voltage
- ECU temperature
- Engine RPM
- Failed-test count
- DTC count

Testing focus:

- Valid numeric input
- Integer vs decimal data
- Expected output
- Basic invalid-input awareness

Independent evidence:

- Automotive measurement recorder/validator built from a Requirement

Mastery target:

- Direct tasks reach INITIAL GREEN if solved independently
- No over-drilling if the concept is already stable

---

# Session 2 - Friday 28 August
## 5 Hours
### Comparisons + Boolean Expressions

Topics:

- `==`
- `!=`
- `<`
- `<=`
- `>`
- `>=`
- Boolean expressions
- Storing comparison results in variables
- Requirement wording to comparison logic

Automotive examples:

- Minimum battery voltage
- Maximum ECU temperature
- RPM threshold
- Communication status

Testing focus:

- Boundary direction
- Exact threshold behavior
- Expected `True` / `False`

Independent evidence:

- Automotive threshold checks written from scratch

---

# Session 3 - Friday 28 August
## 5 Hours
### if / elif / else + Boundary Thinking

Topics:

- `if`
- `elif`
- `else`
- Multiple states
- Ordering conditions
- Inclusive/exclusive boundaries
- Basic `and` / `or` when needed

Automotive example:

Battery Voltage Status Classifier:

- LOW
- NORMAL
- HIGH

ISTQB/Test Design integration:

- Boundary Value Analysis introduction
- Equivalence Partitioning introduction
- Why threshold defects happen

Independent evidence:

- Full Automotive multi-state classifier
- Manual tests including exact boundaries

---

# Session 4 - Saturday 29 August
## 5 Hours
### for Loops

Topics:

- Repetition from a Requirement
- `for`
- `range()`
- Loop variables
- Counters
- Accumulators
- Reusing conditions inside loops

Automotive examples:

- Process a fixed set of ECU test results
- Count PASS / FAIL outcomes
- Validate repeated sensor samples

Testing focus:

- Zero items
- One item
- Multiple items
- Counter correctness

Independent evidence:

- Automotive repeated-result processing task

---

# Session 5 - Saturday 29 August
## 5 Hours
### while Loops + Stop Conditions

Topics:

- When `while` is appropriate
- Loop condition
- Stop condition
- Updating loop state
- Avoiding infinite loops
- Reusing `if` inside `while`

Automotive examples:

- Read ECU samples until a stop condition
- Retry-style learning scenario with a strict limit
- Collect test results until tester ends execution

Testing focus:

- Immediate stop
- Normal stop
- Maximum iterations
- Infinite-loop prevention

Independent evidence:

- Automotive task requiring an explicit stop condition

---

# Session 6 - Sunday 30 August
## 5 Hours
### Strings for Validation and Test Data

Topics:

- String creation
- Indexing
- Slicing
- `strip()`
- `split()`
- `join()`
- `replace()`
- `find()`
- `startswith()`
- `endswith()`
- Basic validation of textual test data

Automotive examples:

- ECU identifier
- Diagnostic response text
- Test-result line
- CAN/log export line

Testing focus:

- Empty string
- Leading/trailing spaces
- Missing separator
- Unexpected status text

Independent evidence:

- Parse and validate an Automotive test-result string

---

# Session 7 - Monday 31 August
## 5 Hours
### Integrated Automotive Problem I

No new major Python topic.

The task must combine several previously learned skills without telling Rizk which constructs to use.

Expected skills may include:

- Input
- Conversion
- Comparisons
- Conditions
- Loops
- Strings

Example direction:

**ECU Measurement Validation Runner**

The exact Requirement should be provided during the session.

Required output:

- Analysis
- Pseudocode
- Code
- Manual tests
- Edge cases

Purpose:

Validate spontaneous recall rather than topic-by-topic prompting.

---

# Session 8 - Tuesday 1 September
## 5 Hours
### Integrated Automotive Problem II + Practical Test Design

A second independent problem with a different shape.

Possible Automotive domains:

- ECU state monitoring
- Battery/temperature/rpm validation
- Diagnostic text processing
- Multiple test-result processing

ISTQB/Test Design integration:

- Test basis
- Test condition
- Test data
- Expected result
- Equivalence Partitioning
- Boundary Value Analysis

The testing technique should be applied to the actual Requirement rather than memorized as a definition.

---

# Session 9 - Wednesday 2 September
## 5 Hours
### Week 01 Assessment + Review + Portfolio Evidence

## Part 1 - Blank-Screen Automotive Assessment

One integrated Requirement.

Rizk independently produces:

- Analysis
- Pseudocode
- Python
- Manual tests
- Edge cases

No automatic hints.

## Part 2 - Debugging Review

Classify issues as:

- Problem Decomposition
- Logic
- Syntax
- Edge Cases
- Testing
- Code Quality

## Part 3 - Mastery Review

For each Week 01 skill decide:

- ORANGE
- INITIAL GREEN
- MASTERED only if there is valid later integrated evidence

## Part 4 - Interview Practice

At least one Python/Test Automation question.

Rizk answers first.

## Part 5 - GitHub / Documentation

- Run final code
- Review `git diff`
- Commit meaningful evidence
- Push
- Update progress tracker
- Record Week 02 priorities

---

# Week 01 Required Outputs

## Code

Automotive-focused implementations demonstrating:

- Input / conversion
- Comparisons
- Conditions
- Loops
- Strings
- Integrated problem solving

## Manual Tests

Representative test cases and expected results.

## Edge Cases

Boundary and negative cases for relevant Requirements.

## Notes

`Python Foundations Rebuild - Week 01` Markdown notes.

## Test Documentation

At least one structured Automotive requirement-to-test example.

## Git

Meaningful professional commits throughout the week.

Suggested prefixes:

```text
feat:
fix:
test:
refactor:
docs:
```

## Interview

At least one reviewed Python/Test Automation interview answer.

## Weekly Review

Update:

- Progress Tracker
- Weaknesses
- Mastery states
- Next-week priorities

---

# Week 01 Success Criteria

Week 01 is complete only if Rizk can demonstrate most of the following:

1. Start a small Automotive program from a Requirement without line-by-line guidance.
2. Identify Input, Output, Variables, Conditions, Repetition, and Stop condition when relevant.
3. Write useful pseudocode before implementation.
4. Select appropriate basic data types.
5. Use comparisons and conditions correctly around boundaries.
6. Use `for` and `while` for different repetition needs.
7. Work with basic strings in testing scenarios.
8. Create meaningful manual tests and edge cases.
9. Debug basic syntax/logic problems without replacing the whole solution.
10. Complete an integrated Automotive assessment.
11. Explain selected decisions in clear technical English.
12. Save meaningful evidence to GitHub.

Weak skills remain ORANGE and are carried forward.

Directly independent skills may become INITIAL GREEN.

MASTERED requires later recall inside integrated work.
