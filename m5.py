# Q5: Persistent Coffee Roast History

import os

# Create folder if it does not exist
os.makedirs("roast_logs", exist_ok=True)

file_name = "roast_logs/roast_history.txt"


# Accept batch details
try:
    batch_id = input("Enter Batch ID: ")
    origin = input("Enter Coffee Origin: ")
    profile = input("Enter Roast Profile: ")

    green_weight = float(input("Enter Green Weight (kg): "))
    loss_percent = float(input("Enter Roast Loss (%): "))

    if green_weight <= 0 or loss_percent < 0 or loss_percent > 30:
        raise ValueError("Invalid weight or roast loss")

    # Calculate roasted weight
    roasted_weight = green_weight - (green_weight * loss_percent / 100)

    # Save batch record
    with open(file_name, "a") as file:
        file.write(
            batch_id + "|" + origin + "|" + profile + "|" +
            str(green_weight) + "|" + str(loss_percent) + "|" +
            str(round(roasted_weight, 2)) + "\n"
        )

    print("\nBatch saved successfully!")

except ValueError:
    print("Error: Please enter valid numeric values.")

# Read saved history
print("\n===== SAVED ROAST HISTORY =====")

valid_count = 0
ignored_count = 0

try:
    with open(file_name, "r") as file:
        for line in file:
            try:
                data = line.strip().split("|")

                if len(data) != 6:
                    raise ValueError

                batch_id, origin, profile = data[0], data[1], data[2]

                green_weight = float(data[3])
                loss_percent = float(data[4])
                roasted_weight = float(data[5])

                print(
                    batch_id, origin, profile,
                    green_weight, loss_percent, roasted_weight
                )

                valid_count += 1

            except ValueError:
                ignored_count += 1

    print("\nValid Records:", valid_count)
    print("Ignored Records:", ignored_count)

    # Display file size
    size = os.path.getsize(file_name)
    print("File Size:", size, "bytes")

except FileNotFoundError:
    print("Error: Roast history file not found.")



"""START

Import the operating system module.

Create the roast_logs folder if it does not exist.

Accept batch details from the user.

Check the numeric values and calculate roasted weight.

If the values are invalid, handle the ValueError.

Otherwise, append the batch details to the history file.

Open the history file and read saved records.

Check each record and skip invalid or incomplete records.

Count the valid and ignored records.

Display all valid records and their counts.

Find and display the file size in bytes.

If the history file is missing, handle FileNotFoundError.

STOP"""