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
