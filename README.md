# Repo Name: Searchable Repository for Text and Images with RAG Integration

## Overview

This repository provides a framework for creating and searching through text and images stored in the repository. The project is designed to handle both text and image data, allowing users to perform searches across the repository efficiently. Additionally, the repository integrates Retrieval-Augmented Generation (RAG) to enhance search capabilities by leveraging advanced retrieval techniques.

**Note:** This project is currently a work in progress. Features and functionalities, including RAG integration, may be incomplete or subject to change.

## Features

- **Text Search:** Efficiently search through text documents in the repository.
- **Image Search:** Perform searches through image files stored in the repository.
- **Retrieval-Augmented Generation (RAG):** Leverages RAG to provide more accurate and contextually relevant search results.
- **Support for Multiple File Formats:** Handles different text formats such as `.txt`, `.pdf`, and `.docx`, and image formats like `.jpg`, `.png`, and `.bmp`.

## Installation

To get started with this project, follow the steps below:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/repo-name.git
    cd repo-name
    ```

2. **Set Up a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**
    All dependencies required for this project are listed in the `requirements.txt` file. Install them using:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Text Search**

    Store your text files in the designated directory (e.g., `/text_files/`). Use the provided Python scripts to search through the content of these files.

2. **Image Search**

    Store your image files in the designated directory (e.g., `/images/`). The provided Python scripts allow you to search images based on their content or metadata.

3. **RAG-Enhanced Search**

    The RAG module enhances search queries by retrieving and generating contextually relevant results, improving the overall accuracy and usefulness of searches across the repository.



## Requirements

This project requires the following Python libraries, which can be installed from the `requirements.txt` file:

- Pillow
- numpy
- lxml
- pdfkit
- python-pptx
- openai
- requests
- and others listed in `requirements.txt`
