# roast_utils.py

import math

# Calculate total roasted output
def total_output(batches):
    total = 0

    for batch in batches:
        total += batch.roasted_weight()

    return total


# Calculate average yield
def average_yield(batches):
    if len(batches) == 0:
        return 0

    total = 0

    for batch in batches:
        total += batch.yield_percent()

    return total / len(batches)


# Calculate number of packs required
def packs_required(roasted_kg, pack_size_kg=0.25):
    return math.ceil(roasted_kg / pack_size_kg)


# Find the batch with the largest roasted weight
def largest_batch(batches):
    if len(batches) == 0:
        return None

    return max(batches, key=lambda batch: batch.roasted_weight())