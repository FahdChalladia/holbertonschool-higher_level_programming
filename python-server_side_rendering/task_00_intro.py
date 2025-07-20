import os

def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    # Check if attendees is a list of dictionaries
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Check if attendee list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for idx, attendee in enumerate(attendees, start=1):
        # Replace placeholders with actual values or "N/A"
        personalized = template
        personalized = personalized.replace("{name}", str(attendee.get("name", "N/A") or "N/A"))
        personalized = personalized.replace("{event_title}", str(attendee.get("event_title", "N/A") or "N/A"))
        personalized = personalized.replace("{event_date}", str(attendee.get("event_date", "N/A") or "N/A"))
        personalized = personalized.replace("{event_location}", str(attendee.get("event_location", "N/A") or "N/A"))

        # Create output file
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(personalized)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
