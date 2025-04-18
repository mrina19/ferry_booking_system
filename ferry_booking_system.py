# Author: Mrinalini, Student ID: 20240984
# This script implements a Ferry Booking System using object-oriented programming in Python.

class FerryBookingSystem:
    ticket_counter = 20000  # Class variable to keep track of ticket IDs

    def __init__(self):
        self.bookings = []  # Initialize an empty list to store bookings (not used here, but good to have just in case of any need)

    # Main method to run the booking process
    def run_booking_system(self):
        print(" Ferry Booking System ")
        print("(Press Enter without typing anything to quit)\n")

        # Start an infinite loop to take multiple bookings
        while True:
            # Ask for ID type (Passport or Driver's License)
            form_of_id = input("Enter the form of ID (Passport, Driver's license): ").strip()
            if form_of_id == "":
                print("\nBooking system closed.")
                break  # Exit the loop if no input is given

            # Ask for ID number and passenger name
            id_num = input("Enter the ID number: ").strip()
            passenger_name = input("Enter the passenger's name: ").strip()

            # Generate a new unique ticket ID
            FerryBookingSystem.ticket_counter += 1
            ticket_id = FerryBookingSystem.ticket_counter

            # Display entered passenger details
            print("\nPrinting Booking Information:")
            print(f"Form of ID: {form_of_id}")
            print(f"ID Number: {id_num}")
            print(f"Passenger Name: {passenger_name}")
            print(f"Ticket ID: {ticket_id}")

            # Start item entry and calculate total price
            total = 0
            print("\nEnter items and their prices. Press Enter without typing anything to quit.")
            while True:
                item = input("Item: ").strip()
                if item.lower() == "":
                    break  # Exit loop if user hits Enter without typing anything

                price = input(f"Price of {item}: $")
                # Check if the price is a valid number
                if price.replace('.', '', 1).isdigit():
                    total += float(price)  # Add valid price to total
                else:
                    print("Invalid price. Try again.")

            print(f"\nTotal: ${total}")  # Show total cost

            # Ask for manager approval and generate status
            status = "Pending"
            decision = input("Manager approval (Y/N): ").strip().lower()
            if decision == "y":
                status = "Approved"
                # Create a reference number using first 3 chars of ID and last 2 digits of ticket ID
                ref_number = id_num[:3] + str(ticket_id)[-2:]
            else:
                status = "Not Approved"
                ref_number = "N/A"

            # Print booking summary
            print("\n Booking Summary ")
            print(f"Form of ID: {form_of_id}")
            print(f"ID Number: {id_num}")
            print(f"Passenger Name: {passenger_name}")
            print(f"Ticket ID: {ticket_id}")
            print(f"Total: ${total}")
            print(f"Status: {status}")
            print(f"Approval Reference Number: {ref_number}")
            print("\n Booking Complete \n")

# Create an instance of the booking system and run it
system = FerryBookingSystem()
system.run_booking_system()
