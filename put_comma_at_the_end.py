def add_comma(input_file, output_file):
    # Open the input file for reading
    with open(input_file, 'r') as f:
        # Read all lines from the input file
        lines = f.readlines()

    # Open the output file for writing
    with open(output_file, 'w') as f:
        # Add a comma at the end of each line and write to the output file
        for line in lines:
            # Strip any leading or trailing whitespace and add a comma
            line = line.strip() + ',\n'
            f.write(line)

# Example usage:
input_filename = input('enter input file path: ')
input_filename = input_filename.replace('"','')
output_filename = input('enter output file path: ')
output_filename = output_filename.replace('"', '')

add_comma(input_filename, output_filename)
print(f"Commas added to lines in {input_filename} and saved to {output_filename}.")
