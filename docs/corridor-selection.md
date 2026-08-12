# Corridor Selection

## Weighted comparison

| Dimension | Weight | India | Nigeria | Source |
|---|---|---|---|---|
| UK corridor size | 20% | £4.17B | £3.90B | ONS-based estimate, via InternationalMoneyTransfer.com Money Transfer Statistics 2025 |
| Fee compression headroom | 25% | Low: already ~1.7-1.8% conversion fee + GST | High: historically 8-10%, compressed to 3-5% by fintech entrants, still moving | Wise India fee breakdown (InfinityApp review); Remitbee 2025 Top Remittance Corridors report |
| Competitive intensity | 20% | High: Wise, Remitly, InstaReM, Xoom, Western Union entrenched | High but fragmented (Sendwave, TransferGo, Africhange, Roze Remit), no dominant leader | Market scan, Phase 0 |
| Structural friction (evidenced) | 25% | High: RBI purpose-code mismatches, FIRA documentation requirements cause delays independent of settlement speed | Moderate: verification delays/limits, largely provider-wide rather than corridor-specific | Wise India user review; provider Trustpilot patterns |
| Data availability | 10% | Good | Good | n/a |

**Weighted score: India 3.65 / Nigeria 4.10** (1-5 scale per dimension)

Note: weights reflect this project's judgement, not an objective standard. Story sharpness (structural friction) was weighted equally with fee headroom. A different weighting could reasonably favour India. This is decided and stated explicitly rather than left implicit.

## Decision

Both corridors carried forward as parallel comparisons, run through the same modelling pipeline (SQL, Excel, Python) rather than built as two separate projects. Corridor is treated as a dimension/field throughout, not a fork.

## Gap statements

**India:** UK→India remittances already operate on thin fee margins (~1.7-1.8% conversion fee plus GST), so incumbents compete on price alone with little room left to disrupt. The evidenced gap is procedural, not economic: RBI purpose-code mismatches and FIRA documentation requirements cause delays independent of settlement speed, and user reviews of established providers cite this friction specifically as the pain point. A purpose-code-aware onboarding flow that pre-validates documentation before the transfer is initiated could reduce delivery failures without competing on an already-compressed margin.

**Nigeria:** The UK→Nigeria corridor has historically carried high fees (8-10%), and while fintech entrants like Wise and WorldRemit have compressed this to 3-5%, the corridor remains fragmented, and no single digital provider holds a dominant position. This leaves real fee-compression headroom on the table, and the competitive gap is structural: a fragmented market with an undifferentiated set of mid-sized players is more winnable than one with an established leader. Corda Remit's opportunity here is pricing-led rather than process-led.

## Caveat

Corridor size figures (£4.17B / £3.90B) come from a secondary aggregator citing ONS balance-of-payments data, not the ONS release directly. Reliable enough for this project's purposes, but not independently verified against the primary source.

## Sources

- [Money Transfer Statistics 2025, InternationalMoneyTransfer.com](https://www.internationalmoneytransfer.com/guides/statistics)
- [Top Remittance Corridors 2025, Remitbee](https://www.remitbee.com/blog/money-transfer/remittance/top-remittance-corridors-2025-fees-market-share)
- [Wise Review: 12 Months of International Payments in India, InfinityApp](https://www.infinityapp.in/blog/wise-review-india)
- [Migrant Remittances to and from the UK, Migration Observatory, Oxford](https://migrationobservatory.ox.ac.uk/resources/briefings/migrant-remittances-to-and-from-the-uk/)
