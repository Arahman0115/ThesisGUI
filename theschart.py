import pandas as pd

# Provided data (replace with actual values)
outcomes = ['Symptom Improvement', 'Response', 'Remission']
guided_care_percentages = [27.1, 27.0, 18.2]
tau_percentages = [22.1, 19.0, 10.7]

# Create a DataFrame
data = {
    'Outcomes': outcomes,
    'Guided-Care Arm (%)': guided_care_percentages,
    'TAU (%)': tau_percentages
}
df = pd.DataFrame(data)

# Display the table
print(df)