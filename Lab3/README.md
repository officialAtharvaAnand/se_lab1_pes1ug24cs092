# Lab 3 Component Modelling and Architectural Pattern Selection

**Atharva Anand | PES1UG24CS092 | Problem Statement 48**  
**System:** Incident Escalation & On-Call Rotation Engine

## Submission

- [Complete submission PDF](Lab3_PES1UG24CS092.pdf): one-page justification followed by the landscape component diagram.
- [Component diagram PDF](Component_Diagram.pdf) and [editable SVG](Component_Diagram.svg).
- [One-page justification PDF](Architecture_Justification.pdf), [Word document](Architecture_Justification.docx), and [text source](Architecture_Justification.md).

The assigned scenario continues [Lab 1 requirements](../requirements.md) and [incident flow](../use-case-flow.md). The coffee kiosk in the Lab 3 handout is its example; this submission models the existing incident system.

## Scenario review

The engine ingests alerts, selects the active engineer, initiates webhook/SMS/email notifications, escalates unacknowledged P1 incidents every five minutes, supports shift overrides, coordinates incident status and ownership, and validates linked post-mortems. The main challenges are reliable timer recovery, acknowledgement/timeout races, correct routing at shift boundaries, a usable acknowledgement flow, and protecting contact data and audit history.

Performance and availability targets come from NFR-001: 99.9% of monthly alerts must create an incident and initiate all configured channels within three seconds; monthly availability must reach 99.95%. The original acceptance criterion mentions p99 at 100 alerts/second, which is weaker than the 99.9% requirement. Validation should therefore check p99.9 as well as the original p99 criterion. No load test or deployed implementation is claimed by this modelling submission.

## Interfaces and responsibilities

A ball belongs to the provider; the socket belongs to the consumer. Solid assembly connectors represent calls, with responses returning over the same interface. Dashed arrows represent usage dependencies. Components are logical modules of a layered application, not independently deployed microservices.

| Interface | Consumer | Provider | Contract / data |
|---|---|---|---|
| IIncident | Operations Console | Incident Coordinator | Authenticated HTTPS/JSON: acknowledge, update, resolve, assign; delegate rotation and post-mortem commands |
| IAlert | Alert API | Incident Coordinator | Internal API: validated alert with source event key, severity, summary and event time; returns incident ID |
| IRotation | Incident Coordinator | Rotation Manager | Internal API: active primary/tier at a timestamp, overrides, publish schedule |
| IEscalation | Incident Coordinator | Escalation Worker | Internal API: persist/cancel timer with incident ID, tier, policy version and due time |
| INotification | Incident Coordinator | Notification Adapter | Internal API: enqueue channel-specific delivery with recipient and idempotency key |
| IPostMortem | Incident Coordinator | Post-Mortem Manager | Internal API: create/update/close linked record after status and mandatory-field validation |
| IStore | Business components | Persistence and Audit | Repository interface implemented with SQL over TLS: state transactions, job claims, outbox, audit append/read |

## Interaction and recovery details

1. Alert API authenticates the monitoring source and deduplicates by source/event key. The coordinator resolves the effective rotation, creates an incident, and commits timer and notification outbox records in one transaction. Duplicate ingestion returns the existing incident ID.
2. The Notification Adapter runs a delivery loop in a background worker, claims outbox rows, and initiates each configured provider call over HTTPS. It records attempts and retries transient failures using bounded backoff and idempotency keys where supported. Outbox commit alone is not notification initiation. Exactly-once delivery across external providers is not assumed.
3. The Escalation Worker claims a persisted due job, locks the incident, rechecks acknowledgement and tier, and atomically advances the tier and writes new delivery jobs. It uses the stored escalation-policy/recipient snapshot. An acknowledgement takes the same incident lock, changes state and cancels pending escalation. Workers check incident state before sending escalation jobs; a provider request already in flight cannot be recalled.
4. Rotation changes and overrides are validated against shift boundaries. New incidents use the current published rotation; active incidents use their policy snapshot unless an authorized reassignment updates it explicitly.
5. Console operations pass through authorization in the business layer. Post-mortem closure verifies that the incident is resolved and all mandatory fields and corrective-action owners are present.
6. Replicated application processes and durable worker claims support restart recovery. A highly available database, backups and failover are required to pursue the availability target. Append-only audit permissions, hash chaining and a separately protected immutable archive provide tamper evidence and 365-day retention.

## Requirement traceability

| Requirement | Components / design support |
|---|---|
| FR-001 Alert routing | Alert API, Incident Coordinator, Rotation Manager, Notification Adapter |
| FR-002 Escalation | Escalation Worker, transactional timer state and notification outbox |
| FR-003 Rotation management | Operations Console, Incident Coordinator, Rotation Manager |
| FR-004 Incident coordination | Operations Console, Incident Coordinator, Persistence and Audit |
| FR-005 Post-mortem tracking | Post-Mortem Manager, incident linkage and validation |
| NFR-001 Performance and availability | Local calls, durable workers, app replicas, database failover; requires measurement |
| NFR-002 Security and auditability | Authenticated entry points, role checks, TLS, AES-256, protected audit retention |

## Handout coverage

- Eight named components across three layers (minimum five).
- Seven named interfaces (minimum four), with provided balls and required sockets on assembly connections.
- Protocol labels, usage dependencies and numbered interaction notes.
- Comparison of Layered, Microservices and Client-Server styles.
- One-page justification with architecture choice, two scenario-specific reasons, security advantage and performance benefit.
- Exported PDF diagram, Word justification and PDF submission under `Lab3/`.

## Sources and assistance

- `Lab_3_Architecture_Student_handout.pdf`, pages 1-7 (course handout).
- Repository `requirements.md` and `use-case-flow.md` (Lab 1 source of truth).
- OpenAI Codex assisted with drafting, diagram construction and document formatting. This is an architectural design, not evidence of an implemented or benchmarked system.
