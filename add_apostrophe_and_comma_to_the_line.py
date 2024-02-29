def quote_and_add_comma(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    modified_lines = ['"' + line.strip() + '",' if line != lines[-1] else '"' + line.strip() + '"' for line in lines]

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(modified_lines))

if __name__ == "__main__":
    input_file_path = input("Enter input file path: ")
    input_file_path = input_file_path.replace('"', '')
    output_file_path = input("Enter output file path: ")
    output_file_path = output_file_path.replace('"', '')

    quote_and_add_comma(input_file_path, output_file_path)

    print("File has been processed and saved successfully.")

   
    
   
    
    

   
