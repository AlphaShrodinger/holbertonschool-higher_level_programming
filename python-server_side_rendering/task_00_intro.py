import os


def generate_invitations(template, attendees):
    # Check if template is empty
    if not isinstance(template, str) or not template.strip():
        print("Error: Template is empty, no output files generated.")
        return []

    # Check if attendees list is empty
    if not isinstance(attendees, list) or not attendees:
        print("Error: No data provided, no output files generated.")
        return []

    # Verify template and attendees data types
    if not isinstance(template, str):
        print("Error: The 'template' parameter must be a string.")
        return []

    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: The 'attendees' parameter must be a list.")
        return []

    generated_files = []

    # Iterate over attendees and write invitations to output files
    for idx, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with values from attendee dictionary
            filled_template = template.replace(
                '{name}', attendee.get('name', 'N/A'))
            filled_template = filled_template.replace(
                '{event_title}', attendee.get('event_title', 'N/A'))
            filled_template = filled_template.replace(
                '{event_date}', attendee.get('event_date', 'N/A'))
            filled_template = filled_template.replace(
                '{event_location}', attendee.get('event_location', 'N/A'))

            # Write to output file
            output_file_name = f"output_{idx}.txt"

            # Check if file already exists
            if os.path.exists(output_file_name):
                print(
                    f"Warning: File '{output_file_name}' already exists.")
            else:
                with open(output_file_name, 'w') as file:
                    file.write(filled_template)
                    generated_files.append(output_file_name)

        except Exception as e:
            print(f"Error writing invitation for attendee {idx}: {str(e)}")

    return generated_files
