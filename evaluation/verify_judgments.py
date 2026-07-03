#!/usr/bin/env python3

"""Verify that topic_judgments.csv reconciles with the published paper
(Tables 2 and 3 of Gordon, 2026; doi:10.18653/v1/2026.nlp4dh-1.21).

Usage:
    python verify_judgments.py [topic_judgments.csv]

Exits nonzero if any check fails.
"""

import sys
from pathlib import Path

import pandas as pd

# Table 2: (n_topics, coherent, thematic)
EXPECTED_TOTALS = {
    "full_k15": (15, 12, 7),
    "full_k60": (60, 48, 37),
    "binned_mallet": (60, 51, 36),
    "binned_authorless": (60, 50, 39),
}

# Table 2: mean over topics.  Binned values
EXPECTED_CONCENTRATION = {
    "full_k15": 0.680,  # are checked only once per-topic values are
    "full_k60": 0.707,  # released for the binned configurations.
    "binned_mallet": 0.807,
    "binned_authorless": 0.727,
}

# Table 3: coherent-AND-thematic per bin
EXPECTED_PER_BIN = {
    "binned_mallet": {
        "pre_1880": 8,
        "1880_1899": 8,
        "1900_1914": 10,
        "1915_1930": 10,
    },
    "binned_authorless": {
        "pre_1880": 10,
        "1880_1899": 9,
        "1900_1914": 9,
        "1915_1930": 11,
    },
}

TOTAL_TOPICS = 195


def main() -> int:
    path = (
        Path(sys.argv[1])
        if len(sys.argv) > 1
        else Path("topic_judgments.csv")
    )
    df = pd.read_csv(path, dtype=str)
    df["concentration"] = pd.to_numeric(df["concentration"], errors="coerce")

    ok = True

    def report(label, got, want):
        nonlocal ok
        match = got == want
        ok &= match
        print(
            f"{'PASS' if match else 'FAIL'} {label}: got {got}, expected {want}"
        )

    report("total topics", len(df), TOTAL_TOPICS)
    report(
        "duplicate (configuration, bin, topic_id) keys",
        int(df.duplicated(["configuration", "bin", "topic_id"]).sum()),
        0,
    )
    report(
        "incoherent rows labeled thematic",
        int(((df["coherent"] == "No") & (df["thematic"] == "Yes")).sum()),
        0,
    )

    for config, (n, coh, them) in EXPECTED_TOTALS.items():
        sub = df[df["configuration"] == config]
        report(f"{config}: n topics", len(sub), n)
        report(
            f"{config}: coherent", int((sub["coherent"] == "Yes").sum()), coh
        )
        report(
            f"{config}: thematic", int((sub["thematic"] == "Yes").sum()), them
        )

    for config, want in EXPECTED_CONCENTRATION.items():
        sub = df[df["configuration"] == config]
        if sub["concentration"].notna().all():
            got = round(float(sub["concentration"].mean()), 3)
            report(f"{config}: mean concentration", got, want)
        else:
            print(
                f"SKIP  {config}: mean concentration "
                f"({int(sub['concentration'].isna().sum())} rows without values)"
            )

    for config, per_bin in EXPECTED_PER_BIN.items():
        sub = df[df["configuration"] == config]
        for bin_name, want in per_bin.items():
            got = int(
                (
                    (sub["bin"] == bin_name)
                    & (sub["coherent"] == "Yes")
                    & (sub["thematic"] == "Yes")
                ).sum()
            )
            report(f"{config} / {bin_name}: coherent-and-thematic", got, want)

    print()
    print("All checks passed." if ok else "One or more checks FAILED.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
