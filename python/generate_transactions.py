"""
Corda Remit — synthetic transaction data generator
Schema: customer_id, signup_month, transaction_date, corridor, amount, fee_revenue

Design choices (documented so they're defensible in an interview):
- 18-month window: Jan 2024 to Jun 2025
- Customers only sign up in the first 12 months, so every cohort has at
  least 6 months of runway to observe retention decay
- Retention decays with tenure (fewer customers stay active the longer
  they've been signed up) rather than being random, so cohort curves look
  like a real business, not noise
- India: larger average transfer (~£380, diaspora sending for education/
  investment/family support), thinner take rate (~1.75%, matches the
  Wise India fee research from Phase 0)
- Nigeria: smaller, more frequent transfers (~£180, regular family
  remittance behaviour), thicker take rate (~4%, matches the fee
  compression story from Phase 0 corridor selection)
- Random seed fixed at 42 for reproducibility
"""

import numpy as np
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

np.random.seed(42)

START_MONTH = date(2024, 1, 1)
TOTAL_MONTHS = 18          # dataset spans Jan 2024 -> Jun 2025
SIGNUP_WINDOW_MONTHS = 12  # customers only sign up in months 0-11

N_CUSTOMERS = 550
CORRIDOR_SPLIT = {"India": 0.55, "Nigeria": 0.45}

# average monthly transactions once active, and £ amount distribution, per corridor
CORRIDOR_PARAMS = {
    "India":   {"avg_amount": 380, "amount_sd": 120, "take_rate": 0.0175, "txns_per_active_month": 1.3},
    "Nigeria": {"avg_amount": 180, "amount_sd": 60,  "take_rate": 0.0400, "txns_per_active_month": 1.8},
}

def month_add(d, n):
    return d + relativedelta(months=n)

def retention_prob(months_since_signup):
    """Probability a customer is still active in a given month since signup.
    Starts near 1.0, decays smoothly, levelling off around a small loyal base."""
    base = 0.35 + 0.65 * np.exp(-months_since_signup / 5.5)
    return np.clip(base, 0.12, 1.0)

customers = []
for i in range(N_CUSTOMERS):
    customer_id = f"CUST{i+1:05d}"
    signup_month_offset = np.random.randint(0, SIGNUP_WINDOW_MONTHS)
    signup_month = month_add(START_MONTH, signup_month_offset)
    corridor = np.random.choice(list(CORRIDOR_SPLIT.keys()), p=list(CORRIDOR_SPLIT.values()))
    customers.append((customer_id, signup_month, corridor))

rows = []
for customer_id, signup_month, corridor in customers:
    params = CORRIDOR_PARAMS[corridor]
    months_available = TOTAL_MONTHS - (signup_month.year - START_MONTH.year) * 12 - (signup_month.month - START_MONTH.month)

    for m in range(months_available):
        p_active = retention_prob(m)
        if np.random.random() > p_active:
            continue  # customer churned by this point, no transactions this month

        n_txns = np.random.poisson(params["txns_per_active_month"])
        n_txns = max(n_txns, 1) if m == 0 else n_txns  # guarantee activity in signup month

        txn_month = month_add(signup_month, m)
        for _ in range(n_txns):
            day = np.random.randint(1, 28)
            transaction_date = date(txn_month.year, txn_month.month, day)
            amount = max(20, np.random.normal(params["avg_amount"], params["amount_sd"]))
            amount = round(amount, 2)
            fee_revenue = round(amount * params["take_rate"] * np.random.uniform(0.9, 1.1), 2)

            rows.append({
                "customer_id": customer_id,
                "signup_month": signup_month.strftime("%Y-%m-%d"),
                "transaction_date": transaction_date.strftime("%Y-%m-%d"),
                "corridor": corridor,
                "amount": amount,
                "fee_revenue": fee_revenue,
            })

df = pd.DataFrame(rows)
df = df.sort_values(["customer_id", "transaction_date"]).reset_index(drop=True)

print(f"Total transactions: {len(df)}")
print(f"Unique customers: {df['customer_id'].nunique()}")
print(f"Date range: {df['transaction_date'].min()} to {df['transaction_date'].max()}")
print(f"\nCorridor split:\n{df['corridor'].value_counts()}")
print(f"\nSample rows:\n{df.head(10)}")

df.to_csv("/home/claude/corda-remit/data/synthetic_transactions.csv", index=False)
print("\nSaved to data/synthetic_transactions.csv")
