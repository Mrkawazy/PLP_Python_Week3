def read_and_modify_file(input_filename, output_filename):
    try:
        # Read the content of the file with utf-8 encoding
        with open(input_filename, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        # Modify the content (e.g., converting to uppercase)
        modified_content = content.upper()
        
        # Write the modified content to a new file
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully wrote to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Cannot read '{input_filename}' or write to '{output_filename}'.")
    except UnicodeDecodeError:
        print(f"Error: The file '{input_filename}' contains characters that cannot be decoded.")

def main():
    input_filename = input("Enter the filename to read from: ")
    output_filename = input("Enter the filename to write to: ")
    
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()