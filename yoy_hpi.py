# Current data uses FHFA's HPI for each month dating all the back to 1991.
# Using a YoY approch is preferred because it's easier for the neural network and will be easier to interpret

# YoY_t = (HPI_t/HPI_(t-12)) -1
# Compares this month's prices to last year's prices at this time
# How do October 2025's prices compare to October 2024's
# This approach is much better for such a large dataset
# Con: I lose the first 12 months of data, because I have no previous year to compare it to, but the dataset still has over 30 years of hpi information.

def hpi_to_yoy(hpi_t, hpi_t12):
    return (hpi_t/hpi_t12) - 1
