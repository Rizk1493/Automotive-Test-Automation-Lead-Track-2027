# Study Method and Mastery Model

## Purpose

This file defines how each topic in the Automotive Test Automation Lead Track 2027 should be taught, practiced, reviewed, and considered complete.

---

# Primary Learning Problem

The main programming gap is not reading code.

The primary gap is:

**Turning a Requirement and a blank screen into structured working code independently.**

Therefore, training should prioritize code generation, decomposition, implementation, testing, and debugging.

---

# Standard Learning Cycle

For each meaningful subtopic:

1. Explain one small concept clearly.
2. Show one complete Automotive example.
3. Explain relevant Edge Cases and Boundary Values.
4. Give one full Automotive task.
5. Rizk solves it independently.
6. Review the result.
7. Repair only demonstrated weaknesses.
8. Continue when understanding is demonstrated.

Do not remain on the same concept through unnecessary repetition.

---

# Independent Task Format

For suitable programming tasks, always use this structure.

## Analysis

```text
Input:
Output:
Variables:
Conditions:
Repetition:
Stop condition:
```

## Pseudocode

Describe the algorithm before implementation.

## Python Code

Implement from a blank screen.

## Manual Test Cases

Include representative inputs and expected outputs.

## Edge Cases

Identify relevant:

- Boundary values
- Invalid values
- Minimum / maximum values
- Empty input where relevant
- Unexpected values
- Negative scenarios
- Timing issues
- Missing communication
- State-related cases

---

# Review Categories

Errors should be classified as:

## Problem Decomposition

The requirement was not broken down correctly.

## Logic

The algorithm or condition is wrong.

## Syntax

The intended logic is correct but Python syntax is wrong.

## Edge Cases

Important boundaries or abnormal situations were missed.

## Testing

The implementation was not verified adequately.

## Code Quality

The code works but has maintainability, naming, structure, or readability issues.

---

# Hint Rule

For independent tasks:

- Do not provide hints automatically.
- Provide the smallest useful hint only when requested or when Rizk is clearly blocked.
- Do not immediately replace buggy code with a full solution.

Preferred repair sequence:

1. Identify the problem area.
2. Give a small hint.
3. Let Rizk attempt the fix.
4. Review the attempt.
5. Provide the final strong solution when appropriate.
6. Explain the engineering lesson.

---

# Mastery States

## ORANGE

Rizk still requires meaningful guidance.

## INITIAL GREEN

Rizk can solve a direct problem independently.

## MASTERED

Rizk can recall and correctly use the concept later inside an integrated problem without being told which concept is required.

A concept should not be marked Mastered after one easy exercise.

A concept also should not be drilled indefinitely after enough evidence exists to progress.

---

# Cumulative Learning Rule

New topics should reuse previous topics whenever practical.

Examples:

```text
Variables + Input/Output
        ↓
Type Conversion
        ↓
Comparisons
        ↓
if / elif / else
        ↓
Loops
        ↓
Strings
        ↓
Collections
        ↓
Functions
        ↓
OOP
        ↓
PyTest
        ↓
Automotive Automation
```

The goal is continuous recall rather than isolated topic completion.

---

# Automotive-First Rule

Meaningful practical exercises should relate to Automotive Testing or Validation whenever possible.

Preferred subjects:

- ECU
- CAN
- LIN
- DBC
- Signals
- CANoe
- CAPL
- UDS
- DTCs
- Diagnostic sessions
- Sensor values
- Test execution
- Test results
- Requirements
- Logs
- Defects
- Validation reports

Generic examples are allowed only when an Automotive example would make the concept unnecessarily confusing.

---

# Edge-Case Rule

Edge cases are a core testing skill, not an optional add-on.

For requirements containing thresholds, ranges, states, timing, counters, messages, or diagnostic conditions, explicitly consider relevant:

- Boundaries
- Equivalence classes
- Invalid inputs
- Minimum / maximum values
- State transitions
- Negative responses
- Timing failures
- Missing communication
- Unexpected responses

---

# Session Continuity Rule

At the beginning of each normal session:

1. Identify where the previous session stopped.
2. Continue from the active roadmap.
3. Review only what is necessary.
4. Do not restart the roadmap.
5. Do not repeatedly ask what topic to study when the plan already defines the next step.

---

# Definition of Strong Understanding

A topic is strong only when Rizk can:

- explain it
- use it
- test it
- recognize edge cases
- apply it later in a different problem
- explain the engineering reason behind the solution
