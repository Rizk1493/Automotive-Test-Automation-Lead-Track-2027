# Tool Stack and Engineering Environment

## Purpose

This file defines the tools used in the Automotive Test Automation Lead Track 2027 and the expected level of competence for each one.

The goal is not to collect tools. Every tool should support a realistic Automotive Validation, Test Automation, Debugging, DevOps, Quality, or Test Lead workflow.

---

# Tier 1 — Must Be Hands-On

These should become everyday or strong working tools.

## Python

Use for:

- Test automation
- Data processing
- Diagnostic automation
- Log analysis
- Reporting
- Utilities around existing automotive tools

## PyTest

Use for:

- Automated test suites
- Fixtures
- Parametrization
- Assertions
- Reports
- Regression automation
- CI execution

## Git

Use continuously for:

- Version control
- Professional commit history
- Branching
- Change review

## GitHub

Use for:

- Portfolio hosting
- Repository documentation
- Pull-request workflow where useful
- GitHub Actions

## VS Code

Primary development environment for:

- Python
- Git
- Markdown
- YAML
- Test execution
- Debugging

## Linux / WSL

Use for:

- Command-line confidence
- Logs
- Processes
- Networking
- Automation execution
- CI-like environments

## CANoe

Use for:

- CAN/LIN analysis
- Trace
- Logging
- Simulation
- Diagnostics
- ECU validation workflows

## CAPL

Use for:

- Event-driven automotive test logic
- Signal/message handling
- Timers
- Diagnostic scenarios

## Wireshark

Use for:

- Packet capture
- Network debugging
- Protocol inspection
- Evidence collection

## Docker

Use for:

- Reproducible test environments
- Running automated tests
- CI-friendly execution

## GitHub Actions

Use for:

- Automated test execution
- Test reports
- Artifacts
- Pass/fail gates

---

# Tier 2 — Automotive Automation and Debugging

## DBC

Working knowledge required for:

- Signal definitions
- Raw/physical conversion
- Scaling and offset
- CAN validation

## UDS

Strong practical knowledge required for:

- Sessions
- Security
- DIDs
- DTCs
- Routine Control
- ECU Reset
- NRCs
- Timing

## python-can

Use where appropriate for:

- CAN scripting
- Simulation
- Test automation integration

Do not confuse virtual CAN behavior with full real-bus behavior.

## Existing UDS Python Libraries

Use existing protocol libraries when appropriate instead of rebuilding the full UDS protocol stack.

The portfolio should focus on validation logic and automation architecture.

## DLT Tools

Use for:

- ECU/application logs
- Filtering
- Error correlation
- Failure evidence

## adb / logcat

Use for:

- Android-based ECU/infotainment debugging
- Log filtering
- Crash investigation

---

# Tier 3 — Supporting Test Automation Breadth

## Robot Framework

Learn enough to:

- Build maintainable tests
- Use keywords/resources
- Integrate Python libraries
- Understand when Robot is more appropriate than PyTest

## REST / API Testing

Use for modern connected-system or general Test Automation readiness.

Topics:

- HTTP
- REST
- JSON
- Authentication basics
- Python requests
- PyTest API validation

## YAML

Use for:

- CI/CD workflows
- Configuration where appropriate

## JSON / CSV

Use for:

- Test data
- Configuration
- Tool exports
- Reports

---

# Tier 4 — Process / Enterprise Tool Awareness

These tools or categories may already exist in professional environments.

The goal is to integrate with them conceptually or through exports rather than rebuild them.

Examples:

- Jira-like defect tracking
- DOORS / requirements-management systems
- Test management systems
- CI dashboards
- Artifact/report systems
- Commercial automotive tools

---

# Do Not Reinvent Rule

Before building a tool, ask:

**Would an Automotive Test/Validation Engineer realistically build or maintain this component at work?**

Avoid rebuilding:

- CANoe
- CANalyzer
- Wireshark
- DLT Viewer
- Jira
- DOORS
- Complete CAN stacks
- Complete UDS stacks
- Full test-management systems

Prefer building automation around existing workflows, exported evidence, or reusable validation logic.

---

# Environment Baseline

Recommended local setup:

```text
Windows
├── VS Code
├── Python
├── .venv
├── Git
├── GitHub
├── WSL / Linux
├── Docker
└── Automotive tooling where available
```

Repository root:

```text
C:\Users\DELL\Documents\Automotive-Test-Automation-Lead-Track-2027
```

---

# Git Workflow

For meaningful sessions:

```text
git status
↓
work
↓
run tests
↓
review diff
↓
git add
↓
git commit
↓
git push
```

Preferred commit styles:

```text
feat: add ECU voltage classification
test: add battery voltage boundary cases
fix: handle invalid diagnostic response
refactor: extract diagnostic response parser
docs: document CAN signal validation approach
ci: run diagnostic regression tests in GitHub Actions
```
