# Lab 3 Architecture Justification

Atharva Anand | PES1UG24CS092

## Architecture selection

We chose Layered Architecture for the Incident Escalation & On-Call Rotation Engine. Presentation and ingestion components call a business layer, which uses a persistence and audit layer. Business modules share one application codebase; durable workers handle timers and delivery.

## Architectural style analysis

Layered: clear module boundaries and local transactions suit this project, but the database can become a bottleneck. Microservices: notification services could scale independently, but distributed acknowledgement and timer state add consistency and operational costs. Client-server: central control is simple, but a basic single-server design limits fault tolerance and does not define internal responsibilities.

## Reason one  Correct escalation

An acknowledgement must stop the five-minute P1 escalation (FR-002 and FR-004). A shared transaction updates incident state and cancels its timer. A worker locks and rechecks state before advancing a tier, avoiding competing acknowledgement and timeout updates.

## Reason two  Maintainable incident workflow

Rotation rules, notification channels and post-mortem validation change independently (FR-001, FR-003 and FR-005). Named interfaces isolate these modules, so a provider adapter or rotation policy can change without rewriting the console or incident coordinator.

## Security advantage

Only authenticated entry points can invoke business operations; role checks restrict schedule changes and incident actions. The data layer uses least-privilege access, TLS 1.2 or later, AES-256 at rest and tamper-evident audit retention of at least 365 days, supporting NFR-002. Layering makes these controls enforceable at defined boundaries; it does not supply encryption by itself.

## Performance benefit and trade-off

Local business calls avoid repeated network hops during routing. A transactional outbox and durable workers decouple provider delays from alert ingestion. The NFR-001 target is to initiate all configured notifications within 3 seconds for 99.9% of monthly alerts at the specified 100-alert/second peak, with 99.95% availability. Replicas, database failover and load tests remain necessary; these are design targets, not measured results.
