
# Author: Mrinalini, Student ID: 20240984
# This script implements a Ferry Booking System using object-oriented programming in Python,
# applying software design principles such as KISS, DRY, SRP, etc.

class FerryBookingSystem:
    ticket_counter = 20000  # Keeps track of ticket IDs globally for uniqueness

    def __init__(self):
        self.bookings = []  # Reserved for future use (Open/Closed principle - extensibility)

    # Main method handling the full booking process
    def run_booking_system(self):
        print(" Ferry Booking System ")
        print("(Press Enter without typing anything to quit)\n")

        while True:
            # KISS: Straightforward user input with clear stopping condition
            form_of_id = input("Enter the form of ID (Passport, Driver's license): ").strip()
            if form_of_id == "":
                print("\nBooking system closed.")
                break  # Exits loop if user presses Enter with no input

            # Clean code > clever code: Descriptive variable names
            id_num = input("Enter the ID number: ").strip()
            passenger_name = input("Enter the passenger's name: ").strip()

            # Ticket ID is generated and incremented (SRP: ideally this should be its own method)
            FerryBookingSystem.ticket_counter += 1
            ticket_id = FerryBookingSystem.ticket_counter

            # DRY Violation: This section could be refactored into a reusable print method
            print("\nPrinting Booking Information:")
            print(f"Form of ID: {form_of_id}")
            print(f"ID Number: {id_num}")
            print(f"Passenger Name: {passenger_name}")
            print(f"Ticket ID: {ticket_id}")

            # Collects service items with prices; tightly coupled, could be extracted (SRP, SoC)
            total = 0
            print("\nEnter items and their prices. Press Enter without typing anything to quit.")
            while True:
                item = input("Item: ").strip()
                if item.lower() == "":
                    break

                price = input(f"Price of {item}: $")
                # Avoid Premature Optimisation: Basic numeric validation without complex parsing
                if price.replace('.', '', 1).isdigit():
                    total += float(price)
                else:
                    print("Invalid price. Try again.")

            print(f"\nTotal: ${total}")  # Direct and user-friendly display (KISS)

            # Approval system (could be separated to follow SRP and Separation of Concerns)
            status = "Pending"
            decision = input("Manager approval (Y/N): ").strip().lower()
            if decision == "y":
                status = "Approved"
                # Reference number logic kept simple (KISS), based on assignment specs
                ref_number = id_num[:3] + str(ticket_id)[-2:]
            else:
                status = "Not Approved"
                ref_number = "N/A"

            # DRY Violation again: repeated summary output should be abstracted (Refactor)
            print("\n Booking Summary ")
            print(f"Form of ID: {form_of_id}")
            print(f"ID Number: {id_num}")
            print(f"Passenger Name: {passenger_name}")
            print(f"Ticket ID: {ticket_id}")
            print(f"Total: ${total}")
            print(f"Status: {status}")
            print(f"Approval Reference Number: {ref_number}")
            print("\n Booking Complete \n")

# YAGNI: No extra features like login, file-saving, etc., since they're not required
# Composition > Inheritance: Simple class structure, no inheritance used unnecessarily
# Code favors readability and correctness over clever tricks or over-engineering

# Instantiating the system and running it
system = FerryBookingSystem()
system.run_booking_system()
