# main.py

import roast_utils
import time


class RoastBatch:

    roastery_name = "Artisan Coffee Roastery"

    def __init__(self, batch_id, origin, roast_profile,
                 green_weight, loss_percent):

        self.batch_id = batch_id
        self.origin = origin
        self.roast_profile = roast_profile
        self.green_weight = green_weight
        self.loss_percent = loss_percent

    def roasted_weight(self):
        return self.green_weight - (self.green_weight * self.loss_percent / 100)

    def yield_percent(self):
        return (self.roasted_weight() / self.green_weight) * 100


# Create batch objects
batch1 = RoastBatch("B104", "Ethiopia", "Medium", 12.5, 16)
batch2 = RoastBatch("B105", "Colombia", "Light", 10, 12)
batch3 = RoastBatch("B106", "Brazil", "Dark", 8, 25)

batches = [batch1, batch2, batch3]

# Store function names in a dictionary
analysis_functions = {
    "1": roast_utils.total_output,
    "2": roast_utils.average_yield,
    "3": roast_utils.packs_required,
    "4": roast_utils.largest_batch
}

print("===== ROAST ANALYSIS =====")
print("1. Total Roasted Output")
print("2. Average Yield")
print("3. Number of Packs Required")
print("4. Largest Batch")

choice = input("Enter your choice: ")

# Record report generation time
report_time = time.strftime("%d-%m-%Y %H:%M:%S")

if choice in analysis_functions:

    if choice == "3":
        result = analysis_functions[choice](
            roast_utils.total_output(batches),
            pack_size_kg=0.25
        )

        print("Packs Required:", result)

    elif choice == "4":
        result = analysis_functions[choice](batches)

        if result is not None:
            print("Largest Batch:", result.batch_id)
            print("Roasted Weight:", round(result.roasted_weight(), 2), "kg")
        else:
            print("No batches available.")

    else:
        result = analysis_functions[choice](batches)

        if choice == "1":
            print("Total Roasted Output:", round(result, 2), "kg")
        else:
            print("Average Yield:", round(result, 2), "%")

    print("Report Generated:", report_time)

else:
    print("Invalid choice!")