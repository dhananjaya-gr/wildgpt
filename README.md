# Hackoholic Bot

## Overview
Hackoholic Bot is a highly maintainable Python-based Generative AI project designed to process and analyze PDF documents and web-scraped content. It uses various libraries and tools to extract, ingest, and split documents, and then create a retriever and chain for further processing.
We designed the cost-effective bot to scrape online data from web pages. The process of opening web pages and extracting data is automated. Our custom open source ollama model generates the rich information on wildlife, biodiversity, and conservation using the gathered knowledge base

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
- `selenium`
- `chrome`
- `python 3.12 (preferred)`
- `huggingface`,
- `frontend`
- `npm`
- `flask`
- `flask_cors`
- `pymupdf`

## Models
```sh
(mrinal_env) (base) mriraj@hackaholic % ollama list
NAME                                                 ID              SIZE      MODIFIED     
nomic-embed-text:latest                              0a109f422b47    274 MB    3 hours ago     
Hackaholics:latest                                   5355ef75aa0b    4.9 GB    37 hours ago    
llama3.1:latest                                      46e0c10c039e    4.9 GB    37 hours ago    
(mrinal_env) (base) mriraj@hackaholic % 
```

## Constants
- `EMBEDDING_MODEL`: 'nomic-embed-text'
- `VECTOR_STORE_NAME`: 'simple_rag'
- `MODEL`: 'llama3.1'
- `DOC_FOLDER`: Path to the folder containing PDF documents
- `RES_FOLDER`: Path to the folder containing resources

## Functions

#### `extract_links_from_pdf(pdf_path)`
Extracts all hyperlinks from a given PDF file from all the pages.

**Parameters:**
- `pdf_path`: The file path to the PDF document.

**Returns:**
- A list of unique URLs found in the PDF.

#### `ingest_pdf(doc_path, folder=False)`
Ingests a PDF file or a folder of PDF files and returns the text content.

**Parameters:**
- `doc_path`: The path to the PDF file or folder.
- `folder`: Boolean indicating if the path is a folder.

**Returns:**
- The text content of the PDF file(s).

#### `split_documents(documents)`
Splits the documents into smaller chunks.

**Parameters:**
- `documents`: The documents to split.

**Returns:**
- The chunks.

#### `create_vector_db(chunks)`
Creates a vector database from the chunks.

**Parameters:**
- `chunks`: The chunks.

**Returns:**
- The vector database.

#### `create_retriever(vector_db, llm)`
Creates a retriever from the vector database and the language model.

**Parameters:**
- `vector_db`: The vector database.
- `llm`: The language model.

**Returns:**
- The retriever.

#### `create_chain(retriever, llm)`
Creates a chain from the retriever and the language model.

**Parameters:**
- `retriever`: The retriever.
- `llm`: The language model.

**Returns:**
- The chain.

#### `createChat()`
Creates a new chat session by sending a POST request to the /chats endpoint.

**Implementation:**
```javascript
async function createChat() {
  const res = await fetch("http://localhost:8000" + "/chats", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
  });
  const data = await res.json();
  if (!res.ok) {
    return Promise.reject({ status: res.status, data });
  }
  return data;
}
```

```javascript
createChat()
  .then(data => {
    console.log("Chat created successfully:", data);
  })
  .catch(error => {
    console.error("Error creating chat:", error);
  });
```

**Details:**

- Method: POST
- URL: http://localhost:8000/chats
- Headers: Content-Type: application/json
- Response: The function returns a promise that resolves to the JSON data from the response if the request is successful. If the request fails, it rejects the promise with an object containing the status code and the response data.


#### `main()`
Main function to run the Hackoholic Bot. It ingests documents, splits them into chunks, creates a vector database, and processes user queries.

## Usage
To run the Hackoholic Bot, use the following command:
```sh
python hackoholic_bot.py
