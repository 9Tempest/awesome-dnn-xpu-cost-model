def parse_entry(entry):
    """Parse an entry into its components."""
    parts = entry.strip().split(';')
    if len(parts) != 3:
        raise ValueError("Each entry must have exactly three parts separated by ';'")
    return parts[0], parts[1], parts[2]

def format_markdown_entry(author, link, citations):
    """Format a single entry into Markdown on one line."""
    return f"- [{author}]({link}) (Citations: {citations})"


def process_input_file(input_file):
    """Process the input file and generate Markdown output."""
    with open(input_file, 'r') as file:
        content = file.read().strip()
    entries = content.split('\n\n')  # Assuming each entry is separated by a blank line
    markdown_output = ""
    for entry in entries:
        author, link, citations = parse_entry(entry)
        markdown_output += format_markdown_entry(author, link, citations) + "\n"
    return markdown_output

input_file = 'cpu_learnt.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print("CPU Learnt Model:")
print(markdown_output)

input_file = 'cpu_analytical.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print("CPU Analytical Model:")
print(markdown_output)

input_file = 'gpu_learnt.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print("GPU Learnt Model:")
print(markdown_output)

input_file = 'gpu_analytical.txt'  # Change this to the path of your input file
markdown_output = process_input_file(input_file)
print("GPU Analytical Model:")
print(markdown_output)
