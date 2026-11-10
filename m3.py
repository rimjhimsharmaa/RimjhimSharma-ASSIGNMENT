# Q3: Coffee Batch Management Using OOP

class RoastBatch:

    roastery_name = "Artisan Coffee Roastery"

    # Constructor
    def __init__(self, batch_id, origin, roast_profile,
                 green_weight, loss_percent):

        self.batch_id = batch_id
        self.origin = origin
        self.roast_profile = roast_profile
        self.green_weight = green_weight
        self.loss_percent = loss_percent

    # Calculate roasted weight
    def roasted_weight(self):
        return self.green_weight - (self.green_weight * self.loss_percent / 100)

    # Calculate yield percentage
    def yield_percent(self):
        return (self.roasted_weight() / self.green_weight) * 100

    # Classify yield
    def classify_yield(self):
        if self.yield_percent() >= 85:
            return "High"
        elif self.yield_percent() >= 75:
            return "Standard"
        else:
            return "Low"

    # Calculate batch value
    def estimate_value(self, price_per_kg):
        return self.roasted_weight() * price_per_kg

    # Display batch details
    def __str__(self):
        return (
            "\nBatch ID: " + self.batch_id +
            "\nOrigin: " + self.origin +
            "\nRoast Profile: " + self.roast_profile +
            "\nGreen Weight: " + str(self.green_weight) + " kg" +
            "\nRoasted Weight: " + str(round(self.roasted_weight(), 2)) + " kg" +
            "\nYield: " + str(round(self.yield_percent(), 2)) + "%" +
            "\nYield Class: " + self.classify_yield()
        )


# Create three objects
batch1 = RoastBatch("B104", "Ethiopia", "Medium", 12.5, 16)
batch2 = RoastBatch("B105", "Colombia", "Light", 10, 12)
batch3 = RoastBatch("B106", "Brazil", "Dark", 8, 25)

# Store objects in a list
batches = [batch1, batch2, batch3]

# Display batch details
print("ROASTERY:", RoastBatch.roastery_name)

for batch in batches:
    print(batch)

# Display estimated values
prices = [1450, 1600, 1300]

print("\n===== BATCH VALUE SUMMARY =====")

for i in range(len(batches)):
    print(batches[i].batch_id, ": Rs.", round(batches[i].estimate_value(prices[i]), 2))

    """
    START

Define a class named RoastBatch.

Declare roastery name as a class variable.

Create a constructor to initialise batch ID, origin,
roast profile, green weight and loss percentage.

Define methods to:
    Calculate roasted weight.
    Calculate yield percentage.
    Classify yield as High, Standard or Low.
    Calculate estimated batch value.
    Display batch details.

Create three objects of the RoastBatch class.

Store all objects in a list.

Display the roastery name and details of each batch.

Calculate and display the estimated value of each batch.

STOP
    """