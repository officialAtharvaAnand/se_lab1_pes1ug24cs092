# Use-Case Flow Specification

## UC-01 - Process and Escalate Incident Alert

| Field | Specification |
|---|---|
| **Primary Actor** | On-Call Engineer |
| **Supporting Actors** | Incident Commander, Monitoring System, Notification Gateway |
| **Trigger** | The Monitoring System sends a valid incident alert. |
| **Preconditions** | An on-call rotation and escalation policy are published; at least one engineer is reachable; notification channels are configured; the Monitoring System is authenticated. |
| **Postconditions (Success)** | The incident is recorded, assigned, acknowledged, and marked in progress; escalation timers are stopped; all actions appear in the audit timeline. |
| **Postconditions (Minimal Guarantee)** | The alert and every delivery or escalation attempt are retained for audit and recovery. |

## Main Success Scenario

1. The Monitoring System submits an alert containing source, severity, summary, and event time.
2. The system validates the alert and creates a uniquely identified incident.
3. The system reads the active rotation and assigns the primary On-Call Engineer.
4. The system sends the incident through the configured webhook, SMS, and email channels.
5. The system starts the acknowledgement timer and records each delivery attempt.
6. The On-Call Engineer opens the incident and selects **Acknowledge** within 5 minutes.
7. The system verifies the engineer's authorization, records the acknowledgement, and stops the escalation timer.
8. The On-Call Engineer sets the incident status to **In Progress** and adds an initial response note.
9. The system stores the update in the incident timeline and notifies the Incident Commander.

## Alternate Flow A1 - No Acknowledgement Within 5 Minutes

1. At Main Flow step 6, the acknowledgement timer expires without a valid acknowledgement.
2. The system records the timeout and selects the next engineer in the configured escalation tier.
3. The system sends notifications to that engineer and starts a new 5-minute timer.
4. Steps A1.2-A1.3 repeat for each remaining tier until an engineer acknowledges the incident.
5. If all tiers expire, the system notifies the Incident Commander, marks the incident **Escalation Exhausted**, and continues retrying according to the emergency policy.
6. When an authorized engineer acknowledges, the flow resumes at Main Flow step 7.
