# Automotive Standards Map

## Purpose

Integrate standards knowledge into the Automotive Test Automation Lead Track 2027 without turning the roadmap into a certification or clause-memorization course.

The target is practical **standards-aware validation**:

> Requirement / protocol expectation → Test condition → Test case → Automation / execution → Evidence → Traceability → Defect / quality decision

Standards are studied inside the engineering topic where they are naturally used.

---

# Learning Depth Model

## PRACTICAL
Rizk should be able to use the standard family as context for realistic validation, test design, debugging, automation, and interview scenarios.

## WORKING AWARENESS
Rizk should understand purpose, vocabulary, lifecycle impact, validation implications, and how it changes evidence or risk thinking.

## AWARENESS
Rizk should understand what the standard is for and when it matters, without pretending specialist or certification-level competence.

Do not memorize clause numbers unless a real job, project, or interview requires them.

---

# Core Communication and Diagnostics Standards

| Standard / Specification | Topic | Target Depth | Roadmap Integration |
|---|---|---|---|
| ISO 11898 series | Controller Area Network (CAN) | PRACTICAL | Week 06 CAN/LIN/DBC |
| ISO 17987 series | Local Interconnect Network (LIN) | PRACTICAL | Week 06 CAN/LIN/DBC |
| ISO 14229 series | Unified Diagnostic Services (UDS) | PRACTICAL | Weeks 08-09 UDS + automation |
| ISO 15765-2 | DoCAN transport/network layer (commonly ISO-TP context) | PRACTICAL | Weeks 08-09 UDS over CAN |
| ISO 13400 series | Diagnostics over Internet Protocol (DoIP) | PRACTICAL | Week 10 Automotive Ethernet/DoIP |
| ISO 21111 series | In-vehicle Ethernet | WORKING AWARENESS | Week 10 network validation |

## Adjacent specifications

These are important but are not all ISO standards:

- IEEE 802.3 — Ethernet foundation.
- AUTOSAR SOME/IP and SOME/IP Service Discovery — service-oriented in-vehicle communication.
- AUTOSAR DLT — Diagnostic Log and Trace.
- Automotive SPICE — process-assessment model; it is not an ISO standard.

The project must name these correctly rather than calling every Automotive specification an ISO standard.

---

# Safety, Cybersecurity, and Quality Standards

## ISO 26262 — Functional Safety

Target: **WORKING AWARENESS for an Automotive Validation / Test Automation Engineer.**

Focus on:

- Functional-safety purpose and lifecycle context
- Safety goals / safety requirements awareness
- ASIL meaning and why rigor changes with risk
- Verification and validation evidence
- Traceability
- Test environment and independence awareness
- Confirmation / review mindset
- Defect and release-risk consequences

Do not position Rizk as a Functional Safety Engineer unless professional evidence supports that.

## ISO/SAE 21434 — Cybersecurity Engineering

Target: **WORKING AWARENESS.**

Focus on:

- Cybersecurity lifecycle context
- TARA awareness
- Cybersecurity requirements
- Verification / validation evidence
- Diagnostic and network attack-surface thinking
- Negative / misuse / access-control testing mindset
- Vulnerability and defect handling awareness

Do not turn the roadmap into a penetration-testing track.

## ISO 21448 — Safety of the Intended Functionality (SOTIF)

Target: **AWARENESS**, especially for ADAS / automated-driving roles.

Focus on:

- Intended-functionality limitations
- Triggering conditions and scenarios
- Known / unknown unsafe scenarios
- Scenario-based validation thinking
- Difference between malfunction-oriented functional safety and intended-functionality limitations

Increase depth only if target job descriptions require ADAS / automated-driving validation.

---

# Optional / Job-Dependent Awareness

Consider only when a target role asks for them:

- IATF 16949 / ISO 9001 quality-management context
- ISO 24089 software update engineering / OTA context
- Additional OEM-specific or domain-specific standards

These are not core roadmap gates unless job-market evidence makes them necessary.

---

# Zero-Cost and Copyright Policy

The study plan does **not** require buying ISO standards.

Use:

- Official ISO catalogue pages, abstracts, and legal previews
- Publicly available technical documentation
- Open-source library documentation
- Public AUTOSAR / protocol documentation where legally available
- Employer-provided or otherwise legally licensed standards if Rizk already has access

Do not:

- Buy standards for this study plan
- Download pirated copies
- Commit copyrighted standards PDFs to GitHub
- Copy large proprietary standard text into portfolio notes

Portfolio notes should summarize concepts in Rizk's own words and reference the standard family.

---

# Evidence Required

For PRACTICAL standards, evidence should include several of:

- Requirement-derived test cases
- Positive / negative cases
- Boundary / timing cases
- State-transition cases
- Trace or packet analysis
- Automated tests
- Failure investigation
- Markdown engineering notes
- Interview explanation
- Traceability to a simulated requirement or protocol expectation

For WORKING AWARENESS standards, evidence should include:

- One concise engineering note
- One validation scenario
- One interview answer
- One Test Lead / risk implication

---

# Portfolio Claim Rule

Use language such as:

- "standards-aware UDS validation"
- "tests designed with ISO 14229 / ISO 15765 context"
- "DoIP validation scenarios aligned with ISO 13400 concepts"
- "functional-safety-aware validation and traceability thinking"

Do **not** claim:

- ISO certification
- formal compliance
- conformance certification
- safety sign-off authority

unless real professional evidence supports the claim.

---

# Mastery Gate

A standard family is not considered ready because Rizk can name it.

For PRACTICAL topics, Rizk should be able to:

1. Explain what engineering problem the standard addresses.
2. Connect it to an Automotive validation workflow.
3. Derive meaningful positive, negative, boundary, timing, or state tests.
4. Interpret relevant test evidence.
5. Explain limitations and what the standard does not prove.
6. Answer a realistic interview follow-up without memorized wording.
