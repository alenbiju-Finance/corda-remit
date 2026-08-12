# Corda Remit

A financial modelling case study: could a digital cross-border payment provider improve UK→India and UK→Nigeria remittances through local settlement, and where does that opportunity actually differ by corridor?

## What Corda Remit does

Corda Remit is a modelled (not real) digital remittance provider using the local-to-local settlement model — holding currency pools in each destination country and netting transfers against them, rather than routing payments through correspondent banking chains. This project builds the unit economics, financial model, and infrastructure cost layer for two UK outbound corridors, to test whether — and how — the opportunity differs between them.

## Corridors

- **UK → India**
- **UK → Nigeria**

Chosen via a weighted comparison across corridor size, fee-compression headroom, competitive intensity, and structural friction — see `docs/corridor-selection.md` for the full scoring and sources.

## Who the customer is

UK-based senders — primarily diaspora communities supporting family, education, or investment needs in India and Nigeria — using a mobile-first digital transfer service in place of banks or cash-based agents.

## The gap it fixes

**India:** UK→India remittances already operate on thin fee margins, so incumbents compete on price with little room left. The evidenced gap is procedural: RBI purpose-code mismatches and FIRA documentation requirements cause delivery delays independent of settlement speed.

**Nigeria:** The UK→Nigeria corridor has historically carried high fees (8-10%), only partially compressed by fintech entrants (down to 3-5%), in a market that remains fragmented with no dominant digital provider. Real fee-compression headroom remains.

Full sourced statements in `docs/corridor-selection.md`.

## How it makes money

- Transaction fees on transfers
- FX spread on conversion
- Float income — interest earned on pooled customer funds held briefly before settlement

## KPIs we track

- **Transfer volume** — the core driver of fee and FX revenue
- **Take rate** — revenue as a % of volume, the key profitability lever per corridor
- **CAC payback period** — how many months until a customer's cumulative revenue covers their acquisition cost
- **Active customers / churn** — retention drives lifetime value, which determines whether acquisition spend is justified
- **Delivery speed vs. competitors** — the operational metric tied directly to the evidenced gap in each corridor

## Project structure

```
corda-remit/
├── README.md
├── docs/
│   └── corridor-selection.md      # Phase 0 scoring table + sources
├── data/                          # synthetic transaction data (Phase 2)
├── sql/                           # cohort, CAC, LTV, payback queries (Phase 2)
└── python/                        # infra cost model (Phase 4)
```

## Progress

- [x] Phase 0 — Research & corridor selection
- [x] Phase 1 — Company narrative
- [ ] Phase 2 — Unit economics in SQL
- [ ] Phase 3 — Three-statement model
- [ ] Phase 4 — Infra cost layer in Python
- [ ] Phase 5 — FX hedging layer
- [ ] Phase 6 — Streamlit dashboard + investment memo
