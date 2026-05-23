# TODO: Golden file test — the central verification moment of Block 4.
# Load tests/golden/may.csv (the pre-built expected output).
# Run receipts report --month 2026-05 --format csv on the ledger populated
# from the 10 inbox samples.
# Assert the output is byte-identical to the golden file.
# NOTE: The golden file is intentionally one row short of what all 10 samples
# produce. The first run will fail. That failure is the teaching moment.
