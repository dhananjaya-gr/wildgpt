# Hackoholic Bot

## Overview
Hackoholic Bot is a Python-based project designed to process and analyze PDF documents and web-scraped content. It uses various libraries and tools to extract, ingest, and split documents, and then create a retriever and chain for further processing.

## Authors
- Mrinal Raj
- Dhananjaya G R
- Sri Sai Pamu
- Shrish Jain

## Dependencies
- `os`
- `re`
- `fitz`
- `ollama`
- `logging`
- `langchain_community.document_loaders`
- `langchain_text_splitters`
- `langchain_community.vectorstores`
- `langchain.prompts`
- `langchain_core.output_parsers`
- `langchain_ollama`
- `langchain_core.runnables`
- `langchain.retrievers.multi_query`
- `webscrap`
- `langchain.schema`

## Constants
- `EMBEDDING_MODEL`: 'nomic-embed-text'
- `VECTOR_STORE_NAME`: 'simple_rag'
- `MODEL`: 'llama3.1'
- `DOC_FOLDER`: Path to the folder containing PDF documents
- `RES_FOLDER`: Path to the folder containing resources

## Functions

### `extract_links_from_pdf(pdf_path)`
Extracts all hyperlinks from a given PDF file from all the pages.

**Parameters:**
- `pdf_path`: The file path to the PDF document.

**Returns:**
- A list of unique URLs found in the PDF.

### `ingest_pdf(doc_path, folder=False)`
Ingests a PDF file or a folder of PDF files and returns the text content.

**Parameters:**
- `doc_path`: The path to the PDF file or folder.
- `folder`: Boolean indicating if the path is a folder.

**Returns:**
- The text content of the PDF file(s).

### `split_documents(documents)`
Splits the documents into smaller chunks.

**Parameters:**
- `documents`: The documents to split.

**Returns:**
- The chunks.

### `create_vector_db(chunks)`
Creates a vector database from the chunks.

**Parameters:**
- `chunks`: The chunks.

**Returns:**
- The vector database.

### `create_retriever(vector_db, llm)`
Creates a retriever from the vector database and the language model.

**Parameters:**
- `vector_db`: The vector database.
- `llm`: The language model.

**Returns:**
- The retriever.

### `create_chain(retriever, llm)`
Creates a chain from the retriever and the language model.

**Parameters:**
- `retriever`: The retriever.
- `llm`: The language model.

**Returns:**
- The chain.

### `main()`
Main function to run the Hackoholic Bot. It ingests documents, splits them into chunks, creates a vector database, and processes user queries.

## Usage
To run the Hackoholic Bot, use the following command:
```sh
python hackoholic_bot.py
