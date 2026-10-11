# GENAI_CONCEPTS

This repository is a hands-on GenAI and document-processing playground. It contains small Python scripts that demonstrate how to load and inspect documents from different sources using LangChain document loaders.

The goal of the project is to practice ingestion pipelines for real-world data before moving into retrieval-augmented generation (RAG), vector search, and AI application development.

## What this project includes

The workspace contains standalone loader scripts for the following data types:

- Text files
- CSV files
- Excel files
- PDF files
- HTML pages
- JSON files
- Markdown files
- Word documents (.docx)
- Directories of text files
- Wikipedia content
- Web-based content

There are also sample files for testing, such as:

- `AggregatedData.csv`
- `dataset.xlsx`
- `sample.json`
- `sample1.html`
- `Raja_Kodumuru_Resume_Updated.pdf`
- `Indian Independence Act, 1947..txt`
- `Bose.docx`

## Project structure

```text
GENAI_CONCEPTS/
├── architecture.md
├── requirements.txt
├── CSV_loader.py
├── Excel_loader.py
├── HTML_loader.py
├── JSON_loader.py
├── Markdown_loader.py
├── PDF_loader.py
├── Text_loader.py
├── WebBased_loader.py
├── Directory_loader.py
├── document_loader.py
├── wiki_loader.py
├── sample.json
├── sample1.html
├── AggregatedData.csv
├── dataset.xlsx
├── Bose.docx
├── Raja_Kodumuru_Resume_Updated.pdf
├── Indian Independence Act, 1947..txt
├── loaders/
│   └── ... virtual environment files
└── README.md
```

## Main idea

Each script usually follows the same pattern:

1. Import a loader from `langchain_community.document_loaders`
2. Point it to a file or source
3. Call `.load()`
4. Print the extracted content and metadata

This is useful for understanding how raw files are converted into document objects that can later be used in:

- vector databases
- semantic search
- RAG pipelines
- summarization systems
- question-answering apps

## Example scripts

### Text loader

`Text_loader.py` loads a `.txt` file and prints the first page of content.

### CSV loader

`CSV_loader.py` loads a CSV file with `CSVLoader` and prints the first record.

### Excel loader

`Excel_loader.py` loads an Excel workbook using `UnstructuredExcelLoader`.

### PDF loader

`PDF_loader.py` uses `PyPDFLoader` to read PDF text.

### HTML loader

`HTML_loader.py` uses `BSHTMLLoader` to extract text from an HTML page.

### Wiki loader

`wiki_loader.py` fetches information from Wikipedia using `WikipediaLoader`.

### Directory loader

`Directory_loader.py` walks through a folder and loads all matching text files.

## Setup

This project depends on Python and several LangChain-related packages.

### 1. Create a virtual environment

```bash
python -m venv loaders
```

### 2. Activate the environment

On Windows PowerShell:

```powershell
.\loaders\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Run a loader

Most scripts are standalone and can be run individually:

```bash
python CSV_loader.py
python PDF_loader.py
python Text_loader.py
python wiki_loader.py
```

## Important note

Several scripts currently use hardcoded local Windows paths such as:

```python
r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\..."
```

These paths should be updated to match your own machine or project location before running them.

## Related file

The project also includes `architecture.md`, which explains a higher-level RAG architecture concept and shows a conceptual system design for advanced AI retrieval workflows.

## Learning objective

This repository is mainly meant for:

- learning document ingestion techniques
- experimenting with LangChain loaders
- preparing data for downstream GenAI workflows
- understanding how raw files become AI-readable content

## Future improvements

Possible next steps for this project include:

- creating a unified loader manager
- adding support for more file types
- building a chunking and indexing pipeline
- integrating with vector databases
- connecting loaders to a simple RAG chatbot

## License

This project is intended for educational and learning purposes.
