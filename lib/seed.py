from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Donor, Recipient, Donation
from faker import Faker
import random

# Database setup
engine = create_engine('sqlite:///blood_donation.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker instance
fake = Faker()

# List of blood types for random selection
blood_types = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]

# Seed data generation using Faker
def seed_data():
    # Generate 10 Donors
    donors = []
    for _ in range(10):
        donor = Donor(
            name=fake.name(),
            phone_number=fake.phone_number(),
            blood_type=random.choice(blood_types),
            age=random.randint(18, 65)
        )
        donors.append(donor)
    session.add_all(donors)

    # Generate 10 Recipients
    recipients = []
    for _ in range(10):
        recipient = Recipient(
            name=fake.name(),
            phone_number=fake.phone_number(),
            blood_type=random.choice(blood_types),
            age=random.randint(18, 65)
        )
        recipients.append(recipient)
    session.add_all(recipients)

    # Generate 10 Donations
    donations = []
    for donor in donors:
        donation = Donation(
            blood_type=donor.blood_type,
            quantity=random.randint(1, 10),  # Random quantity between 1 and 10 units
            donor=donor  # Link donation to a donor
        )
        donations.append(donation)
    session.add_all(donations)

    # Commit the changes to the database
    session.commit()

    # Output confirmation
    print("Database seeded with 10 donors, 10 recipients, and 10 donations.")

if __name__ == "__main__":
    seed_data()
