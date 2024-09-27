from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from tabulate import tabulate

Base = declarative_base()

# Association table for many-to-many relationship between Recipient and Donation
recipient_donation_association = Table(
    'recipient_donation', Base.metadata,
    Column('recipient_id', Integer, ForeignKey('recipients.id')),
    Column('donation_id', Integer, ForeignKey('donations.id'))
)

class Donor(Base):
    __tablename__ = 'donors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    blood_type = Column(String)
    age = Column(Integer)

    # Relationship with Donation
    donations = relationship('Donation', back_populates='donor')

    def __repr__(self):
        return f"Donor {self.name}, ID: {self.id}, Blood Type: {self.blood_type}, Phone: {self.phone_number}"


class Recipient(Base):
    __tablename__ = 'recipients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone_number = Column(String, unique=True, nullable=False)
    blood_type = Column(String)
    age = Column(Integer)

    # Many-to-many relationship with donations through recipient_donation_association
    donations = relationship(
        'Donation',
        secondary=recipient_donation_association,
        back_populates='recipients'
    )

    def __repr__(self):
        return f"Recipient {self.name}, ID: {self.id}, Blood Type: {self.blood_type}, Phone: {self.phone_number}"


class Donation(Base):
    __tablename__ = 'donations'
    id = Column(Integer, primary_key=True)
    blood_type = Column(String)
    quantity = Column(Integer)

    # Relationships
    donor_id = Column(Integer, ForeignKey('donors.id'))
    donor = relationship('Donor', back_populates='donations')

    recipients = relationship(
        'Recipient',
        secondary=recipient_donation_association,
        back_populates='donations'
    )

    def __repr__(self):
        return f"Donation ID: {self.id}, Blood Type: {self.blood_type}, Quantity: {self.quantity}"


# Database setup
engine = create_engine('sqlite:///blood_donation.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# 1. Add Methods
def add_donor():
    # Prompt user for donor information
    name = input("Enter Donor's Name: ")
    phone_number = input("Enter Donor's Phone Number: ")
    blood_type = input("Enter Donor's Blood Type: ")
    age = int(input("Enter Donor's Age: "))

    # Create a new Donor instance
    new_donor = Donor(name=name, phone_number=phone_number, blood_type=blood_type, age=age)
    session.add(new_donor)
    session.commit()
    
    # Print result in a table format
    print(tabulate([[new_donor.id, new_donor.name, new_donor.phone_number, new_donor.blood_type, new_donor.age]], 
                    headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], 
                    tablefmt="fancy_grid"))
    

def add_recipient():
    # Prompt user for recipient information
    name = input("Enter Recipient's Name: ")
    phone_number = input("Enter Recipient's Phone Number: ")
    blood_type = input("Enter Recipient's Blood Type: ")
    age = int(input("Enter Recipient's Age: "))

    # Create a new Recipient instance
    new_recipient = Recipient(name=name, phone_number=phone_number, blood_type=blood_type, age=age)
    session.add(new_recipient)
    session.commit()
    
    # Print result in a table format
    print(tabulate([[new_recipient.id, new_recipient.name, new_recipient.phone_number, new_recipient.blood_type, new_recipient.age]], 
                    headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], 
                    tablefmt="fancy_grid"))
    

def add_blood_type():
    # Prompt user for donor ID
    donor_id = int(input("Enter Donor ID: "))
    # Prompt user for blood type and quantity
    blood_type = input("Enter Blood Type: ")
    quantity = int(input("Enter Quantity: "))

    donor = session.query(Donor).filter_by(id=donor_id).first()
    if donor:
        new_donation = Donation(blood_type=blood_type, quantity=quantity, donor=donor)
        session.add(new_donation)
        session.commit()
        
        # Print result in a table format
        print(tabulate([[donor.name, new_donation.blood_type, new_donation.quantity]], 
                        headers=["Donor Name", "Blood Type", "Quantity"], 
                        tablefmt="fancy_grid"))
    else:
        print("Donor not found")


def delete_donor():
    # Prompt user for donor ID
    donor_id = int(input("Enter Donor ID to delete: "))
    
    donor = session.query(Donor).filter_by(id=donor_id).first()
    if donor:
        session.delete(donor)
        session.commit()
        
        # Print result in a table format
        print(tabulate([[donor.name]], 
                        headers=["Deleted Donor"], 
                        tablefmt="fancy_grid"))
    else:
        print("Donor not found")


def delete_recipient():
    # Prompt user for recipient ID
    recipient_id = int(input("Enter Recipient ID to delete: "))
    
    recipient = session.query(Recipient).filter_by(id=recipient_id).first()
    if recipient:
        session.delete(recipient)
        session.commit()
        
        # Print result in a table format
        print(tabulate([[recipient.name]], 
                        headers=["Deleted Recipient"], 
                        tablefmt="fancy_grid"))
    else:
        print("Recipient not found")


def update_donor():
    donor_id = int(input("Enter Donor ID to update: "))
    donor = session.query(Donor).filter_by(id=donor_id).first()
    
    if donor:
        print(f"Current details: {donor}")
        
        name = input("Enter new name (leave blank to keep current): ")
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        blood_type = input("Enter new blood type (leave blank to keep current): ")
        age_input = input("Enter new age (leave blank to keep current): ")
        age = int(age_input) if age_input else None
        
        if name:
            donor.name = name
        if phone_number:
            donor.phone_number = phone_number
        if blood_type:
            donor.blood_type = blood_type
        if age is not None:
            donor.age = age

        session.commit()
        
        # Print result in a table format
        print(tabulate([[donor.id, donor.name, donor.phone_number, donor.blood_type, donor.age]], 
                        headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], 
                        tablefmt="fancy_grid"))
    else:
        print("Donor not found")

def update_recipient():
    recipient_id = int(input("Enter Recipient ID to update: "))
    recipient = session.query(Recipient).filter_by(id=recipient_id).first()
    
    if recipient:
        print(f"Current details: {recipient}")
        
        name = input("Enter new name (leave blank to keep current): ")
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        blood_type = input("Enter new blood type (leave blank to keep current): ")
        age_input = input("Enter new age (leave blank to keep current): ")
        age = int(age_input) if age_input else None
        
        if name:
            recipient.name = name
        if phone_number:
            recipient.phone_number = phone_number
        if blood_type:
            recipient.blood_type = blood_type
        if age is not None:
            recipient.age = age

        session.commit()
        
        # Print result in a table format
        print(tabulate([[recipient.id, recipient.name, recipient.phone_number, recipient.blood_type, recipient.age]], 
                        headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], 
                        tablefmt="fancy_grid"))
    else:
        print("Recipient not found")


def update_donation():
    donation_id = int(input("Enter Donation ID to update: "))
    donation = session.query(Donation).filter_by(id=donation_id).first()
    
    if donation:
        print(f"Current details: {donation}")
        
        blood_type = input("Enter new blood type (leave blank to keep current): ")
        quantity_input = input("Enter new quantity (leave blank to keep current): ")
        quantity = int(quantity_input) if quantity_input else None
        
        if blood_type:
            donation.blood_type = blood_type
        if quantity is not None:
            donation.quantity = quantity

        session.commit()
        
        # Print result in a table format
        print(tabulate([[donation.id, donation.blood_type, donation.quantity]], 
                        headers=["ID", "Blood Type", "Quantity"], 
                        tablefmt="fancy_grid"))
    else:
        print("Donation not found")


def generate_reports():
    input("Press Enter to generate the blood donation reports...")  # Wait for user input
    
    num_donors = session.query(Donor).count()
    num_recipients = session.query(Recipient).count()
    
    total_blood_quantity = session.query(Donation).with_entities(Donation.quantity).all()
    total_quantity = sum([d[0] for d in total_blood_quantity])

    # Prepare report data
    report_data = [
        ["Number of Donors", num_donors],
        ["Number of Recipients", num_recipients],
        ["Total Blood Quantity Available", f"{total_quantity} units"]
    ]

    print("\n--- Blood Donation Reports ---")
    print(tabulate(report_data, headers=["Description", "Value"], tablefmt="fancy_grid"))


def donate_blood():
    donor_id = input("Enter the Donor ID: ")  # Get donor ID from user
    blood_type = input("Enter the Blood Type (e.g., A+, B-, O+): ")  # Get blood type from user
    quantity = input("Enter the Quantity (in units): ")  # Get quantity from user

    # Validate quantity input
    try:
        quantity = int(quantity)
    except ValueError:
        print("Quantity must be a number.")
        return

    donor = session.query(Donor).filter_by(id=donor_id).first()
    if donor:
        new_donation = Donation(blood_type=blood_type, quantity=quantity, donor=donor)
        session.add(new_donation)
        session.commit()
        
        # Print result in a table format
        print(tabulate([[donor.name, new_donation.blood_type, new_donation.quantity]], 
                        headers=["Donor Name", "Blood Type", "Quantity"], 
                        tablefmt="fancy_grid"))
    else:
        print("Donor not found")

def generate_donors_report():
    donors = session.query(Donor).all()
    if donors:
        report_data = [[donor.id, donor.name, donor.phone_number, donor.blood_type, donor.age] for donor in donors]
        print("\n Donor List ---")
        print(tabulate(report_data, headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], tablefmt="fancy_grid"))
    else:
        print("No donors found.")

def generate_recipients_report():
    recipients = session.query(Recipient).all()
    if recipients:
        report_data = [[recipient.id, recipient.name, recipient.phone_number, recipient.blood_type, recipient.age] for recipient in recipients]
        print("\n--- Recipient List ---")
        print(tabulate(report_data, headers=["ID", "Name", "Phone Number", "Blood Type", "Age"], tablefmt="fancy_grid"))
    else:
        print("No recipients found.")

# Modify the existing generate_reports function to include the new reports
def generate_reports():
    input("Press Enter to generate the blood donation reports...")  
    
    num_donors = session.query(Donor).count()
    num_recipients = session.query(Recipient).count()
    
    total_blood_quantity = session.query(Donation).with_entities(Donation.quantity).all()
    total_quantity = sum([d[0] for d in total_blood_quantity])

    # Prepare report data
    report_data = [
        ["Number of Donors", num_donors],
        ["Number of Recipients", num_recipients],
        ["Total Blood Quantity Available", f"{total_quantity} units"]
    ]

    print("\n--- Blood Donation Reports ---")
    print(tabulate(report_data, headers=["Description", "Value"], tablefmt="fancy_grid"))
    
    # Call new reporting functions
   
    
    
