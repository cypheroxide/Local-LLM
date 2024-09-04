```markdown
# Dynamic Context Retrieval Script for Retrieval Augmented Generation (RAG)

This Python script is designed to enable **Dynamic Context Retrieval** by scanning a directory (knowledge base), extracting relevant information from files based on user queries, and returning contextually relevant snippets. It can be integrated into a locally hosted LLM interface, such as **OpenWeb UI**, to enhance the LLM's responses by providing additional context from files.

## Features

- **Directory Scanning**: Recursively scans a specified directory to find all files.
- **File Type Support**: Extracts text from `.txt`, `.docx`, and `.pdf` files.
- **Keyword-based Matching**: Matches user queries against the contents of files to return relevant information.
- **Context Retrieval**: Returns relevant snippets from files, which can be used for Retrieval Augmented Generation (RAG) tasks.
- **Scalable for RAG Pipelines**: Can be integrated into larger workflows to enhance local LLMs with document-based knowledge.

## Requirements

To use the script, ensure you have Python installed along with the following libraries:

- `python-docx`: For reading `.docx` files.
- `pandas`: Used for handling data but can be extended for `.xlsx` files.
- `PyPDF2`: For extracting text from `.pdf` files.

You can install the required libraries using `pip`:

```bash
pip install python-docx pandas PyPDF2
```

## How It Works

1. **Scan the Knowledge Base**: The script recursively scans a directory (which can be local or network-mounted) for files.
2. **Extract Text**: It supports extracting text from `.txt`, `.docx`, and `.pdf` files.
3. **Search for Relevant Text**: Based on a user-provided query, the script searches through the contents of these files and returns any text that matches the query.
4. **Return Context**: The script returns a snippet (first 500 characters) of matching content along with the file paths where the information was found.

## Usage

### Example Usage in Python

You can run the script directly or integrate it into your local LLM interface:

```python
import os
from pathlib import Path
from docx import Document
import pandas as pd
import PyPDF2

def scan_directory(directory_path):
    """
    Scans the directory and retrieves all files.

    :param directory_path: The path to the knowledge base directory.
    :return: A list of all file paths in the directory.
    """
    files_list = []

    dir_path = Path(directory_path)

    if not dir_path.exists() or not dir_path.is_dir():
        return f"Error: '{directory_path}' is not a valid directory."

    for root, _, files in os.walk(dir_path):
        for file in files:
            full_path = os.path.join(root, file)
            files_list.append(full_path)

    return files_list

def extract_text_from_file(file_path):
    """
    Extracts text from different file types (txt, docx, pdf).

    :param file_path: Path to the file.
    :return: Extracted text as a string.
    """
    extracted_text = ""

    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as file:
            extracted_text = file.read()
    
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        for para in doc.paragraphs:
            extracted_text += para.text + "\n"
    
    elif file_path.endswith('.pdf'):
        try:
            with open(file_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                for page in reader.pages:
                    extracted_text += page.extract_text() + "\n"
        except Exception as e:
            print(f"Error reading PDF file {file_path}: {e}")
    
    return extracted_text

def search_for_relevant_text(query, files):
    """
    Search files for relevant text based on the user's query.

    :param query: The user's query as a string.
    :param files: List of file paths to search in.
    :return: A dictionary of file paths and their matched text sections.
    """
    relevant_info = {}

    for file_path in files:
        text = extract_text_from_file(file_path)

        if query.lower() in text.lower():
            # Store relevant file and matching text
            relevant_info[file_path] = text

    return relevant_info

def retrieve_relevant_context(query, directory_path):
    """
    Main function to retrieve relevant context for a given query.

    :param query: User's query string.
    :param directory_path: Path to the directory (knowledge base).
    :return: Relevant text snippets from matching files.
    """
    files = scan_directory(directory_path)
    
    if isinstance(files, str):
        return files  # If error occurred in scanning

    matched_data = search_for_relevant_text(query, files)

    if matched_data:
        result = f"Found relevant information in {len(matched_data)} file(s):\n"
        for file, content in matched_data.items():
            result += f"\nFile: {file}\n---\n{content[:500]}...\n\n"  # Return the first 500 characters of matched content
        return result
    else:
        return "No relevant information found."

# Example usage
if __name__ == "__main__":
    query = input("Enter your query: ")
    knowledge_base_dir = input("Enter the knowledge base directory path: ")

    context = retrieve_relevant_context(query, knowledge_base_dir)
    print(context)
```

### Example Output

```bash
Enter your query: cybersecurity
Enter the knowledge base directory path: /path/to/knowledge/base
Found relevant information in 2 file(s):

File: /path/to/knowledge/base/file1.txt
---
Cybersecurity refers to the practice of protecting systems, networks, and programs from digital attacks...

File: /path/to/knowledge/base/reports.docx
---
In the 2023 report on cybersecurity trends, it was noted that the rise of ransomware has posed significant challenges...
```

## How to Integrate with OpenWeb UI

To integrate this script with **OpenWeb UI**, you can modify the user inputs and outputs to interface with the UI:

```python
def retrieve_relevant_context_ui(query, directory_path):
    """
    Function to retrieve relevant context in OpenWeb UI.

    :param query: User's query string.
    :param directory_path: Path to the directory (knowledge base).
    :return: Relevant text snippets from matching files or error messages.
    """
    return retrieve_relevant_context(query, directory_path)
```

## Potential Use Cases for Retrieval Augmented Generation (RAG)

This script can be used as a building block for RAG tasks, where documents are used to dynamically enhance responses from a locally hosted LLM:

1. **Document-Based Queries**: Dynamically search a knowledge base to provide relevant content from stored documents during a conversation.
2. **Context Injection**: Automatically inject relevant information from scanned files into the LLM’s context, allowing the model to respond more accurately.
3. **Building Searchable Knowledge Bases**: The scanned files can be indexed and referenced later for faster access to relevant information.

## Extending the Script

- **Add Support for More File Types**: You can extend the `extract_text_from_file` function to support additional formats like `.xlsx`, `.csv`, or even email files.
- **Optimize Matching**: Integrate more advanced search techniques like TF-IDF or semantic search to improve matching performance.
- **Caching for Speed**: Index and cache the files for faster repeated queries.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by **Cypher Oxide**  
GitHub: [https://github.com/cypheroxide](https://github.com/cypheroxide)
```

### Explanation of the Sections

- **Features**: Lists the key functionality of the script.
- **Requirements**: Specifies the Python libraries required to run the script.
- **How It Works**: Describes the script flow from directory scanning to context retrieval.
- **Usage**: Provides an example of how to use the script directly in Python.
- **Integration with OpenWeb UI**: Offers a function ready to be used in the UI.
- **RAG Use Cases**: Suggests how the script can be applied in Retrieval Augmented Generation pipelines.
- **Extending the Script**: Ideas for future improvements, like adding more file types or caching.
- **License and Author**: Standard licensing and author information for GitHub projects.
