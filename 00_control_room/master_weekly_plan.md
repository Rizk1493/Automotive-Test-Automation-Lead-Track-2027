# Master Weekly Plan

## Target Positioning

**Hands-on Automotive Test Automation / Validation Engineer  
with Test Lead / Test Management capability**

## Timeline

- Start: **30 August 2026**
- Core roadmap completion target: **23 January 2027**
- Career target: **Early 2027**
- Study capacity: **45 hours/week**
- One session: **5 hours**
- Normal capacity: **9 sessions/week**

The plan is intensive but evidence-driven. A week may carry unfinished work forward if the required practical mastery is not demonstrated.

---

# Weekly Roadmap

| Week | Dates | Main Focus | Primary Evidence |
|---|---|---|---|
| 01 | 30 Aug-5 Sep | Python Foundations Rebuild I | Blank-screen Automotive programs using input, conversion, conditions, loops, strings, tests and edge cases |
| 02 | 6-12 Sep | Python Foundations II: Collections + Functions | Automotive data-processing tasks using lists/dicts/functions and cumulative fundamentals |
| 03 | 13-19 Sep | Python Engineering + OOP + Problem Solving | Modular Automotive program using files/config, exceptions, OOP, logging and independent decomposition |
| 04 | 20-26 Sep | Git/GitHub + Linux + PyTest Foundations | Daily Git workflow, tester-oriented Linux tasks, first Automotive PyTest suite |
| 05 | 27 Sep-3 Oct | Professional PyTest Automation | Fixtures, parametrization, markers, conftest, test data, reports, mocking basics, framework structure |
| 06 | 4-10 Oct | CAN + LIN + DBC Rebuild + ISO 11898 / ISO 17987 Context | CAN/LIN validation scenarios, DBC/raw-to-physical reasoning, signal edge cases, standards-aware protocol explanation |
| 07 | 11-17 Oct | CANoe + CAPL Confidence Rebuild | Realistic trace/debugging scenarios, CAPL event/timer/test logic; commercial tooling only where legal access exists |
| 08 | 18-24 Oct | UDS / Diagnostics + ISO 14229 / ISO 15765-2 | Session/service/NRC/DTC/transport test design with positive, negative, timing and state cases |
| 09 | 25-31 Oct | UDS Automation + ECU Validation | Python/OOP/PyTest diagnostic regression components using existing protocol/tool abstractions with standards-aware traceability |
| 10 | 1-7 Nov | Automotive Ethernet + DoIP + SOME/IP + Wireshark + ISO 13400 / ISO 21111 Context | Packet inspection, DoIP/SOME-IP validation thinking, Wireshark evidence, transport/network failure cases |
| 11 | 8-14 Nov | DLT + adb/logcat + Failure Debugging + HIL/SIL/System Integration | Multi-source failure investigation, HIL/SIL role awareness, integration/system validation scenarios |
| 12 | 15-21 Nov | Requirements-Based Testing + Practical ISTQB Test Design | Requirement review, traceability, EP, BVA, Decision Tables, State Transition tests |
| 13 | 22-28 Nov | Software Quality + ASPICE + Defect Management + ISO 26262 / ISO/SAE 21434 Awareness | Quality/ASPICE evidence, professional defect reports, safety/cybersecurity-aware validation scenarios, triage and regression thinking |
| 14 | 29 Nov-5 Dec | Robot Framework + API Testing | Maintainable Robot tests and PyTest/API validation without losing Automotive focus |
| 15 | 6-12 Dec | Docker + CI/CD + GitHub Actions | Real project tests executed in reproducible environment with CI reports/artifacts/gates |
| 16 | 13-19 Dec | Flagship Project 1 - Diagnostic Regression Framework I | Architecture, requirements, configuration, diagnostic abstractions, initial automated tests, standards-context traceability |
| 17 | 20-26 Dec | Flagship Project 1 - Diagnostic Regression Framework II | Expanded regression suite, reporting, traceability, CI, documentation, standards context and limitations |
| 18 | 27 Dec-2 Jan | Test Management + Test Leadership + Risk-Based Testing | Planning, estimation, prioritization, coverage, defect triage, quality/reporting, standards/evidence risk and release scenarios |
| 19 | 3-9 Jan | Flagship Project 2 - Failure Evidence Correlator | Correlate exported CAN/diagnostic/DLT/logcat/test evidence around failures |
| 20 | 10-16 Jan | Validation Coverage Checker + Quality/Defect Portfolio Integration | Requirements/tests/results reconciliation, coverage reporting, quality/defect/release evidence |
| 21 | 17-23 Jan | Final Integration + Portfolio + Full Mock Interviews + Gap Closure | Job-readiness assessment, GitHub hardening, integrated technical/Lead mock interviews including standards context |

---

# Important Sequencing Rules

## Python Is a Foundation, Not the Destination

Weeks 01-03 are Python-heavy.

From Week 04 onward Python becomes an engineering tool used inside:

- PyTest
- CAN/UDS automation
- Log processing
- Debugging
- CI/CD
- Portfolio projects

Do not keep extending Python fundamentals indefinitely once practical readiness is demonstrated.

## Git Is Continuous

Git/GitHub are used from Week 01.

Week 04 deepens Git and Linux; it does not mark the first time Git is used.

## ISTQB Is Integrated

ISTQB Foundation concepts are studied where they improve real engineering work, not as an exam track.

Examples:

- Weeks 01-03: test basis, test conditions, expected results, edge cases
- Week 05: regression, confirmation, testware, automation risks
- Weeks 08-10: state/negative/timing test design
- Week 12: EP, BVA, Decision Tables, State Transition, static testing
- Weeks 13 and 18: defects, risk, planning, monitoring/control, reporting

## Automotive Standards Are Integrated

Standards are not a separate theory week.

Use `automotive_standards_map.md` as the reference map.

Integration:

- Week 06: ISO 11898 (CAN) + ISO 17987 (LIN)
- Weeks 08-09: ISO 14229 (UDS) + ISO 15765-2 (DoCAN / transport)
- Week 10: ISO 13400 (DoIP) + ISO 21111 / IEEE 802.3 Ethernet context; SOME/IP remains AUTOSAR context
- Week 13: ISO 26262 Functional Safety + ISO/SAE 21434 Cybersecurity working awareness
- Week 18: standards evidence, risk, traceability and release implications from a Test Lead perspective
- ISO 21448 SOTIF: awareness; increase depth if an ADAS-focused role requires it

Do not turn standards learning into clause memorization or certification cramming.

## Automotive Ethernet / DoIP / SOME/IP

These are explicitly preserved as job-readiness topics.

They are studied after CAN/UDS foundations so the protocol and debugging context is meaningful.

## HIL / SIL / System and Integration Validation

The goal is practical validation understanding and interview readiness.

Do not fabricate hardware access or professional HIL experience.

Use realistic test architecture, environment, interface, fault-isolation, and validation scenarios.

---

# Portfolio Strategy

The major projects are:

1. **ECU Diagnostic Regression Automation Framework**
2. **Automotive Failure Evidence Correlator**
3. **Automotive Validation Coverage Checker**

Before building anything ask:

> **Would an Automotive Test/Validation Engineer realistically build or maintain this at work?**

Do not rebuild mature commercial tools such as CANoe, CANalyzer, Wireshark, Jira, DOORS, DLT viewers, complete CAN/UDS stacks, or a full test-management system.

Build useful validation automation around existing workflows, tool exports, APIs, and protocol libraries.

Portfolio work may demonstrate **standards-aware validation** but must not claim formal ISO compliance, certification, or conformance authority without real evidence.

---

# Weekly Required Evidence

A normal week should produce meaningful evidence from several of:

- Working code
- Automated tests
- Automotive hands-on tasks
- Manual test cases
- Edge cases / boundary values
- Markdown notes
- Requirements/test documentation
- Defect/quality evidence
- Standards-aware test rationale where relevant
- Git commits
- Interview practice
- Test Lead scenarios
- Progress updates

A week is not complete merely because its topics were explained.

---

# Mastery Model

## ORANGE
Needs guidance or is not yet practically validated.

## INITIAL GREEN
Can perform a direct task independently.

## MASTERED
Can recall and apply the skill later inside integrated work without prompting.

Progress is evidence-based, not self-rating based.

---

# Final Job-Readiness Gate

By the final phase Rizk should be able to demonstrate:

- Blank-screen Automotive automation from Requirements
- Maintainable PyTest automation
- CAN/LIN/DBC reasoning and debugging
- Standards-aware CAN/LIN understanding using ISO 11898 / ISO 17987 context
- CANoe/CAPL validation thinking where legal tool access exists
- UDS/diagnostics test design and automation with ISO 14229 / ISO 15765 context
- Automotive Ethernet/DoIP/SOME-IP working knowledge with ISO 13400 and relevant Ethernet context
- HIL/SIL and System/Integration validation understanding
- Failure investigation using traces/logs/network evidence
- Requirements-based test design and practical ISTQB techniques
- Defect and Software Quality capability
- ASPICE explanation connected to evidence and traceability
- Functional-safety and cybersecurity awareness relevant to validation work
- Git/Linux/Docker/CI/CD working skills
- Risk-based Test Lead decisions
- Professional technical English
- GitHub portfolio evidence supporting these claims
