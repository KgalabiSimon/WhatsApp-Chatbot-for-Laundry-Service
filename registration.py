


def handle_registration(message_body, from_number):

    details = message_body.split(',')
    if len(details) == 4:
        #add user to the database
        print(details[0]+details[1]+details[2] +details[3])
        response_message = "Registration complete. Thank you!"
    else:
        response_message = "Please provide your details in the format: Name,Surname,DOB,Residence"
            
    return response_message