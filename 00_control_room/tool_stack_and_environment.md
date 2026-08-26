# Tool Stack and Engineering Environment

## Purpose

This file defines the tools used in the Automotive Test Automation Lead Track 2027 and the expected level of competence for each one.

The goal is not to collect tools. Every tool should support a realistic Automotive Validation, Test Automation, Debugging, DevOps, Quality, Standards, or Test Lead workflow.

---

# Cost and Access Rule

The study and portfolio stack is **zero-cost**.

Default to:

- Free / open-source tooling
- Free public documentation
- GitHub public-repository capabilities
- Simulation and exported evidence

Commercial tools may be used only when Rizk already has legitimate access.

Do not require purchasing:

- CANoe / CANalyzer / Vector licenses
- Commercial HIL hardware
- Paid ALM tools
- Paid ISO standards
- Paid Docker products

Do not use pirated tools or standards.

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
- Utilities around existing Automotive tools

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

## Ubuntu / Linux

Use the Ubuntu laptop for:

- Command-line confidence
- Logs
- Processes
- Networking
- Docker Engine
- SocketCAN / `vcan`
- `can-utils`
- Automation execution
- CI-like environments

A WSL Linux distribution is not required while the separate Ubuntu machine is available.

## Wireshark / TShark

Use for:

- Packet capture
- Network debugging
- Protocol inspection
- Evidence collection
- DoIP / Ethernet validation scenarios

Windows baseline includes Wireshark/TShark with Npcap for live capture.

## adb / logcat

Use for:

- Android-based ECU/infotainment debugging
- Log filtering
- Crash investigation

Windows Android Platform Tools are part of the prepared baseline.

## Docker Engine

Prefer Docker Engine on Ubuntu for:

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

## DBC / `cantools`

Working knowledge required for:

- Signal definitions
- Raw/physical conversion
- Scaling and offset
- CAN validation

Install/use `cantools` when the CAN/DBC phase starts.

## `python-can`

Use where appropriate for:

- CAN scripting
- Simulation
- Test automation integration

Do not confuse virtual CAN behavior with full real-bus behavior.

## SocketCAN / `vcan` / `can-utils`

Use on Ubuntu for:

- Free CAN workflow practice
- Virtual CAN simulation
- Sending/receiving frames
- Trace/log practice
- Integration with Python CAN tooling

Simulation is explicitly labeled as simulation and not equivalent to physical-bus/HIL validation.

## UDS Libraries

Use existing libraries rather than rebuilding protocol stacks.

Likely stack when the UDS phase starts:

- `udsoncan`
- `can-isotp` or an appropriate ISO-TP abstraction
- `doipclient` where useful

Select versions when the phase starts rather than installing everything in advance.

## DLT Tools

Use open-source tooling where practical for:

- ECU/application logs
- Filtering
- Error correlation
- Failure evidence

---

# Tier 3 — Access-Dependent Commercial Automotive Tools

## CANoe

Use hands-on only if legal access exists.

Relevant workflows:

- CAN/LIN analysis
- Trace
- Logging
- Simulation
- Diagnostics
- ECU validation

If access is unavailable:

- refresh workflow/interview knowledge
- use legal exported evidence
- use free CAN tooling and simulation for transferable validation skills
- do not claim the free tooling is a full CANoe replacement

## CAPL

Use hands-on only with legal CANoe/CANalyzer-compatible access.

Focus on:

- Event-driven Automotive test logic
- Signal/message handling
- Timers
- Diagnostic scenarios

Preserve previous professional exposure accurately without claiming current tool access if unavailable.

---

# Tier 4 — Supporting Test Automation Breadth

## Robot Framework

Learn enough to:

- Build maintainable tests
- Use keywords/resources
- Integrate Python libraries
- Understand when Robot is more appropriate than PyTest

## REST / API Testing

Use:

- Python `requests`
- PyTest
- Thunder Client already available
- `curl`

Topics:

- HTTP
- REST
- JSON
- Authentication basics
- Negative testing

No paid API client is required.

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

# Standards and Specification References

Standards knowledge is part of engineering context, not a software-tool installation.

Core map:

- ISO 11898 — CAN
- ISO 17987 — LIN
- ISO 14229 — UDS
- ISO 15765-2 — DoCAN transport/network layer
- ISO 13400 — DoIP
- ISO 21111 — In-vehicle Ethernet context
- ISO 26262 — Functional Safety awareness
- ISO/SAE 21434 — Cybersecurity Engineering awareness
- ISO 21448 — SOTIF awareness

Adjacent:

- IEEE 802.3 — Ethernet
- AUTOSAR SOME/IP / Service Discovery
- AUTOSAR DLT
- Automotive SPICE — not ISO

See `automotive_standards_map.md` for learning depth and evidence.

## Reference Access Policy

Do not buy standards for this roadmap.

Use:

- official ISO catalogue/abstract pages and legal previews
- public technical documentation
- open-source library documentation
- public protocol/specification documentation where legally available
- employer-provided licensed standards if legitimately accessible

Do not commit copyrighted standards PDFs or large copied clauses to GitHub.

---

# Tier 5 — Process / Enterprise Tool Awareness

These tools or categories may already exist in professional environments.

The goal is to integrate with them conceptually or through exports rather than rebuild them.

Examples:

- Jira-like defect tracking
- DOORS / requirements-management systems
- Test management systems
- CI dashboards
- Artifact/report systems
- Commercial Automotive tools

Use GitHub Issues, Markdown, CSV, JSON and sample exports for portfolio evidence instead of purchasing enterprise tools.

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
- Complete UDS / ISO-TP / DoIP stacks
- Full test-management systems

Prefer building automation around existing workflows, exported evidence, protocol libraries, and reusable validation logic.

---

# Environment Baseline

## Windows — Primary Automotive Workstation

```text
Windows
├── VS Code
├── Python 3.11 project .venv
├── Git / GitHub / gh
├── Wireshark / TShark / Npcap
├── adb / fastboot
└── Commercial Automotive tooling only if legal access exists
```

## Ubuntu — Linux / DevOps / Simulation Workstation

```text
Ubuntu
├── Git / GitHub
├── Python
├── Docker Engine
├── Bash / Linux networking
├── SocketCAN / vcan / can-utils
├── tcpdump / Wireshark
├── adb / logcat where useful
└── Project test execution
```

GitHub is the bridge between the two machines.

Do not manually duplicate project copies outside normal Git clone/pull/push workflows.

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
docs: map automotive standards to validation phases
ci: run diagnostic regression tests in GitHub Actions
```
