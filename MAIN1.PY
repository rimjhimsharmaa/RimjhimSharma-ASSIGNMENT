# Q2: Multiple Coffee Batch Management

# Dictionary for roast profiles
profiles = {
    "Light": "L",
    "Medium": "M",
    "Dark": "D",
    "Espresso": "E"
}

batches = {}
origins = set()

while True:
    batch_id = input("\nEnter Batch ID (or DONE to stop): ")

    if batch_id.upper() == "DONE":
        break

    origin = input("Enter Coffee Origin: ")
    profile = input("Enter Roast Profile (Light/Medium/Dark/Espresso): ").title()

    # Check roast profile
    if profile not in profiles:
        print("Invalid roast profile! Batch rejected.")
        continue

    green_weight = float(input("Enter Green Weight (kg): "))
    loss_percent = float(input("Enter Roast Loss (%): "))

    # Validate weight and loss
    if green_weight <= 0:
        print("Invalid weight! Batch rejected.")
        continue

    if loss_percent < 0 or loss_percent > 30:
        print("Invalid roast loss! Batch rejected.")
        continue

    # Calculate roasted weight and yield
    weight_lost = green_weight * loss_percent / 100
    roasted_weight = green_weight - weight_lost
    yield_percent = (roasted_weight / green_weight) * 100

    # Classify yield
    if yield_percent >= 85:
        yield_class = "High"
    elif yield_percent >= 75:
        yield_class = "Standard"
    else:
        yield_class = "Low"

    # Store valid batch
    batches[batch_id] = {
        "origin": origin,
        "profile": profiles[profile],
        "green_weight": green_weight,
        "roasted_weight": roasted_weight,
        "yield_percent": yield_percent,
        "yield_class": yield_class
    }

    origins.add(origin)

    print("Batch added successfully!")

# Display batch summary
print("\n===== ROASTERY SUMMARY =====")

total_green = 0
total_roasted = 0

for batch_id, details in batches.items():
    total_green += details["green_weight"]
    total_roasted += details["roasted_weight"]

    print(batch_id, "-", details["yield_class"])

print("\nTotal Batches:", len(batches))
print("Total Green Weight:", round(total_green, 2), "kg")
print("Total Roasted Output:", round(total_roasted, 2), "kg")
print("Unique Coffee Origins:", origins)

# Sort batches by roasted weight
print("\n===== BATCHES SORTED BY ROASTED WEIGHT =====")

sorted_batches = sorted(
    batches.items(),
    key=lambda item: item[1]["roasted_weight"]
)

for batch_id, details in sorted_batches:
    print(batch_id, ":", round(details["roasted_weight"], 2), "kg")

"""
START

Create a dictionary of available roast profiles.
Create an empty dictionary to store batches.
Create an empty set to store unique origins.

REPEAT:

    Accept batch ID.
    If batch ID is DONE, stop accepting batches.

    Accept coffee origin and roast profile.

    Check whether the roast profile is valid.
    If invalid, reject the batch and continue.

    Accept green weight and roast loss percentage.

    Check whether weight is positive and loss is between 0 and 30.
    If invalid, reject the batch and continue.

    Calculate roasted weight and yield percentage.

    Classify the yield as High, Standard or Low.

    Store valid batch details in the dictionary.
    Add the coffee origin to the set.

UNTIL the user enters DONE.

Calculate total green weight and roasted output.
Display batch count and unique coffee origins.
Sort batches according to roasted weight.
Display the sorted batch details.

STOP
    


"""