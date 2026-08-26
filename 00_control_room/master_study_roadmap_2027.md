# Automotive Test Automation Lead Track 2027

## Master Study Roadmap

### Central Objective

Become job-ready by early 2027 as a:

**Hands-on Automotive Test Automation / Validation Engineer with Test Lead / Test Management capability.**

The target is not a pure developer, pure manual tester, or pure manager.

The final profile combines:

- Automotive Validation
- Test Automation
- Automotive Diagnostics
- Automotive Standards Awareness
- Debugging
- DevOps for Testing
- Software Quality
- Defect Management
- Requirements-Based Testing
- Test Management
- Test Leadership

---

# Study Capacity

- Sunday-Thursday: 5 hours/day
- Friday: 10 hours
- Saturday: 10 hours
- Total: **45 hours/week**
- One session: **5 hours**
- Normal weekly capacity: **9 sessions**

Time must be balanced between learning, independent implementation, Automotive practice, testing/quality, portfolio evidence, interviews, and leadership.

---

# Learning and Mastery Principle

The primary coding-development target is:

> **Requirement → Analysis → Pseudocode → Working Code → Tests → Edge Cases → Review**

Use:

- ORANGE
- INITIAL GREEN
- MASTERED

A direct successful task can establish INITIAL GREEN.

MASTERED requires later independent use inside integrated work without prompting.

---

# Standards Integration Principle

Automotive standards are integrated into the engineering phase where they matter.

The project does **not** add a separate ISO-theory week and does not require buying standards.

Core mapping:

- ISO 11898 series → CAN
- ISO 17987 series → LIN
- ISO 14229 series → UDS
- ISO 15765-2 → DoCAN transport/network layer
- ISO 13400 series → DoIP
- ISO 21111 series → In-vehicle Ethernet context
- ISO 26262 → Functional Safety working awareness for validation
- ISO/SAE 21434 → Cybersecurity Engineering working awareness
- ISO 21448 → SOTIF awareness, deeper only for ADAS-focused roles

Adjacent specifications must be named correctly:

- IEEE 802.3 → Ethernet foundation
- AUTOSAR SOME/IP / Service Discovery → service-oriented Automotive communication
- AUTOSAR DLT → Diagnostic Log and Trace
- Automotive SPICE → process-assessment model, not an ISO standard

Detailed learning depth, evidence rules, copyright constraints and portfolio-claim boundaries are defined in `automotive_standards_map.md`.

---

# Phase 0 - Environment and Engineering Workflow

## Objectives

- Stabilize VS Code workflow
- Confirm Python virtual environment
- Confirm Git/GitHub workflow
- Preserve existing repository work
- Use professional Markdown notes
- Define weekly evidence and mastery tracking
- Maintain a zero-cost study environment unless legal commercial access already exists

## Expected Evidence

- Working environment
- Clean repository workflow
- Professional Git commits
- Updated control room files

---

# Phase 1 - Python Foundations Rebuild

## Topics

- Variables
- Input / Output
- Data Types
- Type Conversion
- Comparisons
- Boolean Expressions
- `if / elif / else`
- `for`
- `while`
- Strings
- Lists
- Dictionaries
- Tuples
- Sets
- Functions
- Files
- Exceptions
- Modules
- Packages
- Virtual environments
- Basic debugging
- OOP

## Main Goal

The main target is not syntax recall.

It is the ability to transform an Automotive Requirement into structured working code from a blank screen.

## Automotive Practice

Examples:

- Battery Voltage Validator
- ECU Temperature Classifier
- RPM Range Monitor
- CAN Signal Value Validator
- DTC Counter
- ECU State Checker
- Test Result Analyzer
- Diagnostic Response Parser

## Exit Criteria

Rizk can independently build a small Automotive program using multiple Python fundamentals, manual test cases, and edge cases without being told which construct to use.

---

# Phase 2 - Engineering Problem Solving for Test Automation

## Focus

- Requirement understanding
- Problem decomposition
- Data selection
- State / condition identification
- Repetition and stop conditions
- Edge-case reasoning
- Refactoring large scripts into smaller responsibilities

## Typical Problems

- ECU Signal Validation
- Multi-signal Test Result Summary
- DTC List Analysis
- Diagnostic Response Classification
- Automotive Test Data Processing

## Exit Criteria

Rizk can independently decide the required inputs, outputs, data structures, conditions, loops, functions, and test cases from an engineering Requirement.

---

# Phase 3 - Git, GitHub, and Linux

## Git / GitHub

- status / diff / add / commit / log
- push / pull
- branches
- merge
- conflict basics
- `.gitignore`
- professional commit messages
- repository organization

Git is used continuously from the start of the project.

## Linux

Tester-oriented skills:

- navigation
- files/directories
- permissions
- `cat`
- `less`
- `head`
- `tail`
- `grep`
- `find`
- pipes
- redirection
- processes
- environment variables
- networking basics
- log investigation

---

# Phase 4 - PyTest Foundations and Professional Automation

## Topics

- Test discovery
- Assertions
- Test organization
- Fixtures
- Fixture scopes
- Parametrization
- Markers
- `conftest.py`
- Test data
- Exception testing
- Setup / teardown concepts
- Configuration
- Reports
- Mocking fundamentals
- Reusable helpers

## Automotive Direction

```text
tests/
├── diagnostics/
├── can/
├── ecu/
└── integration/
```

## Exit Criteria

Rizk can structure and maintain an Automotive-oriented PyTest suite instead of only writing standalone scripts.

---

# Phase 5 - CAN / LIN / DBC Rebuild

## Standards Context

- ISO 11898 series — CAN
- ISO 17987 series — LIN

The goal is not clause memorization. Rizk should connect protocol behavior to validation evidence and realistic failure cases.

## CAN

- frame structure
- Standard / Extended identifiers
- arbitration
- DLC
- payload
- signals
- raw / physical values
- scaling / offset
- bit positions
- byte order
- DBC
- timing
- bus load
- error concepts

## LIN

- commander/responder terminology awareness and common master/slave terminology used in industry
- schedule tables
- frames
- signals
- timing
- common use cases
- CAN vs LIN

## Hands-On Focus

- Decode signals
- Validate ranges
- Detect timeouts
- Investigate wrong scaling
- Analyze missing frames
- Build realistic validation scenarios
- Explain which behavior is protocol-level, database-level, tool-level, or application-level

---

# Phase 6 - CANoe and CAPL Confidence Rebuild

## Access Rule

CANoe/CAPL are commercial. Use them hands-on only if legal access already exists.

Do not buy licenses for this roadmap.

If legal access is unavailable, preserve interview/workflow confidence using prior experience, exported traces/configuration examples where legally shareable, free CAN tooling, and realistic scenarios without claiming equivalent CANoe execution.

## CANoe

- Configuration structure
- Trace
- Measurement
- Logging
- DBC integration
- Simulation
- Nodes
- Panels
- System / environment variables
- Diagnostics

## CAPL

- Event-driven model
- CAN events
- Timers
- Variables
- Functions
- Signal handling
- Diagnostic events
- Test logic

## Exit Criteria

Rizk can explain and work through realistic ECU communication/signal investigation scenarios using CANoe/CAPL concepts and clearly state actual tool access limitations.

---

# Phase 7 - UDS / Automotive Diagnostics

## Standards Context

- ISO 14229 series — UDS application/session concepts
- ISO 15765-2 — DoCAN transport/network layer for UDS over CAN

Distinguish application-layer diagnostic behavior from transport-layer segmentation/flow behavior.

## Foundations

- Request / Response
- Positive Response
- Negative Response
- NRCs
- Diagnostic timing
- Diagnostic sessions
- Preconditions
- Application vs transport responsibilities
- Single-frame vs multi-frame transport reasoning
- Flow-control awareness

## Core Services

- `0x10` Diagnostic Session Control
- `0x11` ECU Reset
- `0x14` Clear Diagnostic Information
- `0x19` Read DTC Information
- `0x22` Read Data By Identifier
- `0x27` Security Access
- `0x2E` Write Data By Identifier
- `0x28` Communication Control
- `0x31` Routine Control
- `0x3E` Tester Present

## Test Design

For services consider:

- Positive cases
- Negative cases
- Preconditions
- Session dependencies
- Security dependencies
- NRC behavior
- Timing
- Recovery behavior
- State transitions
- Transport segmentation / flow / timeout cases where applicable

---

# Phase 8 - UDS Automation and ECU Validation

Combine:

- Python
- OOP
- PyTest
- UDS
- ECU state
- Logging
- Configuration
- Reporting
- Standards-aware traceability

Build automation around existing protocol/tooling rather than implementing a complete UDS stack from scratch.

The automation should test ECU behavior; it should not become a homemade UDS/ISO-TP stack project.

---

# Phase 9 - Automotive Ethernet, DoIP, SOME/IP, and Network Validation

## Standards / Specification Context

- ISO 13400 series — DoIP
- ISO 21111 series — In-vehicle Ethernet context
- IEEE 802.3 — Ethernet foundation
- AUTOSAR SOME/IP / Service Discovery — not ISO

## Automotive Ethernet

Develop practical validation/interview knowledge around:

- Ethernet fundamentals required for testing
- MAC/IP/UDP/TCP context
- network interfaces
- packet flow
- addressing
- timing and connectivity failures

## DoIP

Focus on testing and diagnostics context:

- Diagnostic communication over IP
- vehicle discovery / announcement awareness
- routing activation / connection workflow awareness
- addressing/routing concepts
- transport/network failure reasoning
- UDS-over-DoIP validation scenarios
- evidence using Wireshark/TShark

## SOME/IP

Focus on working validation knowledge:

- service-oriented communication concepts
- service / method / event concepts
- discovery awareness
- request/response vs event behavior
- validation and debugging scenarios

## Wireshark

Use for:

- packet capture
- display filters
- protocol inspection
- timing/evidence correlation

## Important Boundary

The goal is practical validation and debugging knowledge, not implementing Ethernet/DoIP/SOME-IP stacks from scratch.

---

# Phase 10 - Robot Framework and API Testing

## Robot Framework

- Tests
- Keywords
- Variables
- Libraries
- Resource files
- Tags
- Setup / teardown
- Reports
- Python integration

## API Testing

- HTTP basics
- REST
- Methods
- Status codes
- Headers
- JSON
- Authentication basics
- Python requests
- PyTest API testing

## Goal

Build supporting modern Test Automation breadth without replacing the Automotive core.

---

# Phase 11 - Automotive Debugging and Logs

## DLT

- AUTOSAR DLT context
- APID / CTID concepts
- Log levels
- Filtering
- Timestamps
- Error correlation

## Android

- `adb`
- `logcat`
- Tags
- Levels
- Filters
- Crash traces

## Network / Test Evidence

Reuse Wireshark, CAN traces, diagnostic logs, PyTest logs, and CI logs.

## Investigation Workflow

```text
Failed Test
↓
Reproduce
↓
Collect Evidence
↓
Correlate timestamps
↓
Identify symptom
↓
Form hypothesis
↓
Narrow component
↓
Collect stronger evidence
↓
Defect / RCA direction
```

---

# Phase 12 - HIL / SIL + System and Integration Validation

## Goal

Strengthen practical validation architecture and interview readiness without fabricating unavailable hardware experience.

## Topics

- Unit / component / integration / system validation context
- SIL purpose and limitations
- HIL purpose and limitations
- Real ECU vs simulated environment
- Interfaces and dependencies
- Stimulus / response thinking
- Fault injection concepts
- Environment configuration
- Test repeatability
- Timing and communication concerns
- Failure isolation across components
- Test evidence and traceability

## Hands-On Direction

Use realistic architecture/scenario exercises and available simulation where appropriate.

Do not pretend simulation equals real HIL hardware behavior.

---

# Phase 13 - Requirements-Based Testing and Practical Test Design

## Requirements

- Requirement analysis
- Ambiguity
- Missing information
- Conflicting requirements
- Testability
- Acceptance criteria
- Traceability
- Requirement coverage
- Distinguish project requirements from standards-derived expectations

## Practical ISTQB Techniques

- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table Testing
- State Transition Testing
- Regression Testing
- Confirmation Testing
- Static testing / review thinking

The goal is practical job readiness, not certification memorization.

---

# Phase 14 - Software Quality, ASPICE, Functional Safety, Cybersecurity Awareness, and Defect Management

## Software Quality

- QA vs QC
- Testing
- Verification
- Validation
- Product quality
- Process quality
- Reviews
- Audits
- Defect prevention
- RCA
- Metrics
- Continuous improvement
- Release quality

## ASPICE

Automotive SPICE is not an ISO standard.

Focus on validation relevance:

- Requirements
- Traceability
- Verification
- Integration
- Qualification testing
- Work products
- Evidence
- Reviews
- Process discipline

## ISO 26262 Functional Safety — Working Awareness

Focus on validation relevance:

- Functional-safety lifecycle purpose
- Safety goals / requirements awareness
- ASIL meaning and rigor implications
- Verification / validation evidence
- Traceability
- review / independence awareness
- safety-related defect and release-risk thinking

Do not position Rizk as a Functional Safety Engineer without real professional evidence.

## ISO/SAE 21434 Cybersecurity Engineering — Working Awareness

Focus on:

- Cybersecurity lifecycle context
- TARA awareness
- Cybersecurity requirements
- diagnostic/network attack-surface thinking
- negative / misuse / access-control validation
- evidence and vulnerability/defect handling awareness

Do not turn the track into a penetration-testing specialization.

## ISO 21448 SOTIF — Awareness

Understand purpose, triggering conditions/scenarios and why intended-functionality limitations differ from malfunction-oriented functional safety.

Increase depth if an ADAS / automated-driving target role requires it.

## Defect Management

Engineer-level:

- Identify
- Reproduce
- Collect evidence
- Write quality defects
- Verify fix
- Regression

Lead-level:

- Triage
- Severity / Priority review
- Aging
- Trends
- Reopened / escaped defects
- Blockers
- Release risk
- Escalation
- Quality communication

---

# Phase 15 - Test Management and Test Leadership

## Test Management

- Test strategy
- Scope
- Planning
- Estimation
- Prioritization
- Risk-Based Testing
- Coverage
- Execution tracking
- Entry / Exit criteria
- Metrics
- Reporting
- Release recommendation
- Standards-derived evidence and compliance-claim boundaries

## Leadership

- Task distribution
- Blocker handling
- Mentoring
- Test review
- Defect conflicts
- Deadline pressure
- Stakeholder communication
- Risk escalation
- Release decisions

Recurring question:

> **What changes if Rizk is the Test Lead?**

Lead-level standards thinking includes asking which requirements, evidence, reviews, independence, traceability, and residual risks matter — not pretending to be the certification authority.

---

# Phase 16 - Docker and CI/CD

## Docker

- Images
- Containers
- Dockerfile
- Build
- Run
- Volumes
- Environment variables
- Networking basics
- Compose basics

## CI/CD

- Workflow
- Trigger
- Dependency setup
- Automated tests
- Reports
- Artifacts
- Pass/fail gates
- GitHub Actions

## Goal

Run real Automotive test automation through the pipeline rather than demo-only tests.

---

# Portfolio Phase

## Flagship Project 1 - ECU Diagnostic Regression Automation Framework

A realistic automation layer for ECU diagnostic validation.

Demonstrates:

- Python
- OOP
- PyTest
- UDS
- ECU Validation
- ISO 14229 / ISO 15765 standards context
- Configuration
- Logging
- Reporting
- Traceability
- CI/CD
- Test design

Do not implement a complete CAN, UDS, or ISO-TP protocol stack.

Do not claim formal ISO conformance; demonstrate standards-aware test design and traceability.

---

## Flagship Project 2 - Automotive Failure Evidence Correlator

Consume exported evidence such as:

- Test failure timestamp
- CAN trace export
- DLT export
- logcat
- diagnostic log
- network evidence

Produce:

- Failure time window
- Relevant messages/errors
- Diagnostic activity
- Evidence timeline
- Investigation summary

Do not build another CANoe Trace, DLT Viewer, or Wireshark replacement.

---

## Portfolio Project 3 - Automotive Validation Coverage Checker

Consume exported:

- Requirements
- Test cases
- Automation results
- optional standards-context tags / source categories

Check:

- Requirement without test
- Test without requirement
- Missing trace links
- Failed requirements
- Coverage

Do not rebuild DOORS, Jira, or a complete ALM platform.

---

# Practical ISTQB Integration

ISTQB Foundation concepts are integrated in their natural engineering phases.

Examples:

- Fundamentals / test basis / expected results during early coding/testing
- Test levels/types during PyTest and system/integration work
- Regression / confirmation during automation and defect work
- EP / BVA / Decision Tables / State Transition during Requirement/Test Design work
- Static testing during Requirement reviews
- Risk-Based Testing during Test Management
- Defect Management during Quality/Defect phases
- Tool support/automation risks during automation and CI/CD

No certification-cramming unless explicitly requested.

---

# Standards Learning and Access Policy

The roadmap does not require purchasing ISO standards.

Use legal public sources and summaries, open tooling documentation, and employer-provided licensed copies if available.

Do not commit copyrighted standards documents or copied proprietary clauses to GitHub.

Focus on engineering understanding and evidence, not memorizing edition numbers. When edition-specific behavior matters, confirm the current applicable edition at study time.

---

# Interview Preparation

Interview practice runs continuously.

## Technical Areas

- Python / PyTest
- CAN / LIN / DBC + ISO 11898 / ISO 17987 context
- CANoe / CAPL
- UDS / Diagnostics + ISO 14229 / ISO 15765 context
- Automotive Ethernet / DoIP / SOME/IP + ISO 13400 context
- HIL / SIL / System & Integration Validation
- Requirements / Test Design
- Defects / Quality / ASPICE
- Functional Safety / Cybersecurity awareness
- Debugging
- CI/CD
- Git / Linux

## Leadership Areas

- Planning
- Estimation
- Prioritization
- Risk
- Coverage
- Defect triage
- Release decisions
- Stakeholder communication
- Mentoring

---

# Final Success Criteria

By early 2027, Rizk should be able to:

- Build Python test automation from Requirements
- Build and maintain PyTest suites
- Explain and debug CAN/LIN behavior and connect it to relevant ISO families
- Work confidently with UDS and ECU diagnostics, including application vs transport responsibilities
- Use CANoe/CAPL confidently where legal access exists and accurately describe access limitations otherwise
- Demonstrate practical Automotive Ethernet/DoIP/SOME-IP validation knowledge
- Explain the role of ISO 13400 in DoIP validation
- Explain HIL/SIL and System/Integration validation practically
- Analyze Automotive logs and failures
- Turn Requirements into effective test designs
- Apply practical ISTQB test techniques
- Create high-quality defects
- Lead defect triage and quality discussions
- Use Git/GitHub professionally
- Use Linux and Docker for test workflows
- Run automated tests through CI/CD
- Explain ASPICE and Software Quality concepts practically
- Explain ISO 26262 / ISO/SAE 21434 implications from a validation-engineer perspective without overstating experience
- Recognize ISO 21448 SOTIF relevance for ADAS-focused validation
- Plan, prioritize, and report testing as a Test Lead
- Communicate confidently in technical English interviews
- Support these claims with a professional Automotive-focused GitHub portfolio
