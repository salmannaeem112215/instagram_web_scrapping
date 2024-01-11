def extract_content(file_path, start_string, end_string, output_file="output.html"):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            start_index = file_content.find(start_string)
            end_index = file_content.find(end_string, start_index)

            if start_index != -1 and end_index != -1:
                extracted_content = file_content[start_index: end_index + len(end_string)]
                with open(output_file, 'w', encoding='utf-8') as output:
                    output.write(extracted_content)
                print(f"Content between '{start_string}' and '{end_string}' extracted and saved to {output_file}")
            else:
                print(f"Strings '{start_string}' and/or '{end_string}' not found in the file.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
file_path = "instagram.html"
start_string = "<main"
end_string = "</main>"
extract_content(file_path, start_string, end_string)
