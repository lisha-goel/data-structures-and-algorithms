import csv
from faker import Faker

fake = Faker()

# Set the seed for reproducibility
Faker.seed(0)

# Generate 3000 rows of data
data = [['Name', 'Mobile Number', 'Age', 'Company']]
for _ in range(3000):
    name = fake.name()
    mobile_number = fake.phone_number()
    age = fake.random_int(18, 65)
    company = fake.company()

    data.append([name, mobile_number, age, company])

# Write to CSV file
with open('generated_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file 'generated_data.csv' has been created.")
