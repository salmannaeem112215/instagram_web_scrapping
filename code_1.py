def extract_links(file_path, link_prefix="href=\"https://www.instagram.com/p/"):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            links = []
            index = file_content.find(link_prefix)
            
            while index != -1:
                end_index = file_content.find("\"", index + len(link_prefix))
                if end_index != -1:
                    link = file_content[index: end_index]
                    links.append(link)
                    index = file_content.find(link_prefix, end_index)
                else:
                    break

            if links:
                with open("output_links.txt", 'w', encoding='utf-8') as output:
                    for link in links:
                        output.write(link + "\n")
                print(f"Links extracted and saved to output_links.txt")
            else:
                print(f"No links found in the file with the specified pattern.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")

# Example usage
file_path = "instagram.html"
extract_links(file_path)
