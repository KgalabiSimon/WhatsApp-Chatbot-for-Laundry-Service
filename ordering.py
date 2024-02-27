



def order():
    laundry_services = ["Dry Cleaning", "Wash & Fold", "Ironing", "Stain Removal"]

    message = "Please select a laundry service:\n"
    for i, service in enumerate(laundry_services, 1):
        message += f"{i}. {service}\n"

    return message

# When a user makes a selection, you can handle it with another function
def handle_selection(message_body, from_number):
    laundry_services = ["Dry Cleaning", "Wash & Fold", "Ironing", "Stain Removal"]

    if message_body.isdigit() and 1<= int(message_body) <= len(laundry_services):

        selected_service = laundry_services[int(message_body) - 1]

        reply =  f"You have selected {selected_service}. Your order has been placed!"
    else:
        reply =  "Sorry, I didnt understand that. Please send order to see the list of services, or a number to select a service."

    return reply


