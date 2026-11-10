# Q1: Coffee Roasting Batch and Yield Tracker

# Accept batch details
batch_id = input("Enter Batch ID: ")
origin = input("Enter Coffee Origin: ")
green_weight = float(input("Enter Green Bean Weight (kg): "))
loss_percent = float(input("Enter Roast Loss (%): "))
roasting_time = int(input("Enter Roasting Time (minutes): "))
price_per_kg = float(input("Enter Selling Price per kg (Rs.): "))

# Display data types
print("\n--- Data Types ---")
print("Green Weight:", type(green_weight))
print("Loss Percentage:", type(loss_percent))

# Calculate roasting details
weight_lost = green_weight * loss_percent / 100
roasted_weight = green_weight - weight_lost

yield_percent = (roasted_weight / green_weight) * 100

batch_value = roasted_weight * price_per_kg

# Convert time into hours and minutes
hours = roasting_time // 60
minutes = roasting_time % 60

# Generate short batch code using slicing
batch_code = batch_id[:2] + "-" + origin[:3].upper()

# Display final report
print("\n===== ROASTING BATCH REPORT =====")
print("Batch ID:", batch_id)
print("Origin:", origin)
print("Batch Code:", batch_code)

print("Green Weight:", green_weight, "kg")
print("Weight Lost:", round(weight_lost, 2), "kg")
print("Roasted Weight:", round(roasted_weight, 2), "kg")
print("Yield Percentage:", round(yield_percent, 2), "%")

print("Roasting Time:", hours, "hours", minutes, "minutes")
print("Selling Price: Rs.", price_per_kg, "/kg")
print("Estimated Batch Value: Rs.", round(batch_value, 2))

"""

START

INPUT batch ID, coffee origin, green weight,
      roast loss percentage, roasting time and price per kg.

DISPLAY the data types of green weight and roast loss.

CALCULATE the weight lost during roasting.

SUBTRACT the weight lost from green weight
to get the roasted weight.

CALCULATE the yield percentage and estimated batch value.

CONVERT roasting time into hours and minutes
using division and modulus operators.

CREATE a short batch code using string slicing.

DISPLAY the batch details and calculated results.

STOP

"""