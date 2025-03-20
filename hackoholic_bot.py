##########################################
#  Authors:
#      1. Mrinal Raj
#      2. Dhananjaya G R
##########################################

# MODEL = 'Hackaholics'

import os
import re
import fitz
import ollama
import logging
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import OllamaEmbeddings
from webscrap import WebscrapOnlineResearch
from langchain.schema import Document

EMBEDDING_MODEL = 'nomic-embed-text'
VECTOR_STORE_NAME='simple_rag'
MODEL = 'llama3.1'

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.WARNING)

DOC_FOLDER = os.path.join(os.path.dirname(__file__), "Index/")
RES_FOLDER = os.path.join(os.path.dirname(__file__), "Resources/")
# DOC_FOLDER = "/Users/dguntira/Desktop/Sustainability/Index/"
# DOC_FOLDER = "https://conbio.onlinelibrary.wiley.com/doi/10.1111/csp2.13096"
#DOC_FOLDER = os.path.join(os.path.dirname(__file__), "Index")
#DOC_FOLDER = "/Users/dguntira/Desktop/Sustainability/Resources/"
def extract_links_from_pdf(pdf_path):
    """
    Extracts all hyperlinks from a given PDF file from all the pages.

    :param pdf_path: The file path to the PDF document.
    :return: A list of unique URLs found in the PDF.
    """
    links = []
    # Open the PDF
    pdf_document = fitz.open(pdf_path)

    # Iterate through all pages
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]

        # Extract text to search for embedded links
        text = page.get_text("text")

        # Find all URLs in the text using regex
        urls = re.findall(r'https?://[^\s]+', text)
        links.extend(urls)

        # Extract hyperlinks from annotations
        for link in page.get_links():
            if 'uri' in link:
                links.append(link['uri'])
    pdf_document.close()
    # Remove duplicates
    return list(set(links))

def ingest_pdf(doc_path, folder=False):
    """
    Ingests a PDF file or a folder of PDF files and returns the text content.

    :param doc_path: the path to the PDF file or folder
    :param folder: boolean indicating if the path is a folder
    :return: the text content of the PDF file(s)
    """
    global web_scrap_obj
    if not folder:
        if doc_path.startswith('http') and doc_path.endswith('.pdf') :
            loader = OnlinePDFLoader(doc_path)
            data = loader.load()
            logging.info("Online PDF Loaded successfully")
            return data
        elif doc_path.endswith('.pdf'):
            loader = UnstructuredPDFLoader(doc_path, mode='multi')
            data = loader.load()
            logging.info("Unstructured PDF Loaded successfully")
            return data
        else:
            logging.info("Webscraping the online research paper")

            web_scrap_obj = WebscrapOnlineResearch()
            data = web_scrap_obj.get_page_source_as_string(doc_path)
            return data
    else:
        data_pool = list()
        all_links = []
        for file in os.listdir(doc_path):
            if file.endswith('.pdf'):
                loader = UnstructuredPDFLoader(os.path.join(doc_path, file))
                links = extract_links_from_pdf(os.path.join(doc_path, file))
                data = loader.load()
                logging.info(f"Unstructured PDF Loaded successfully {file}")
                data_pool.append(data[0])
                all_links.extend(links)
        unique_links = list(set(all_links))
        return data_pool, unique_links

def split_documents(documents):
    """
    Split the documents into smaller chunks.

    :param documents: the documents to split
    :return: the chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
    if isinstance(documents, str):
            documents = [Document(page_content=documents)]  
    # Convert your string into Document objects
    # documents = [Document(page_content="This is the first document."),
    #             Document(page_content="This is the second document.")]

    # # Now, you can safely call split_documents
    # chunks = text_splitter.split_documents(documents)
    chunks = text_splitter.split_documents(documents)
    logging.info("Done splitting")
    logging.info(f"Number of chunks: {len(chunks)}")
    return chunks

def create_vector_db(chunks):
    """
    Create a vector database from the chunks.

    :param chunks: the chunks
    :return: the vector database
    """
    # Load the embeddings model from https://ollama.com/library/nomic-embed-text
    ollama.pull(EMBEDDING_MODEL)
    vector_db = Chroma.from_documents(documents=chunks,embedding= OllamaEmbeddings(model=EMBEDDING_MODEL),collection_name= VECTOR_STORE_NAME)
    logging.info("Vector DB created...")
    return vector_db

def create_retriever(vector_db, llm):
    """
    Create a retriever from the vector database and the language model.

    :param vector_db: the vector database
    :param llm: the language model
    :return: the retriever
    """
    QUERY_PROMPT = PromptTemplate(input_variables=["question"], #template="\f'{context_template}' Original question: {question}")
                                  template="""You are an AI language model assistant named as Hackaholic.
                                  Your task is to generate seven different versions of the question given by user to retrieve relevant documents from a vector database.
                                  By generating multiple perspectives on the question by user, your goal is to help the user overcome some of the limitations of the distance-based similarity search.
                                  Provide these alternative questions separated by newlines. Make sure to give enough information which covers the aspects of What, Why, When, Where, Who, How, and Which.
                                  Also, initially before recieving your first query introduce yourself and start with a list of all the things you can do.
                                  Original question: {question}""")

    retriever = MultiQueryRetriever.from_llm(vector_db.as_retriever(), llm=llm, prompt=QUERY_PROMPT)
    logging.info("Retriever created...")
    return retriever

def create_chain(retriever, llm):
    """
    Create a chain from the retriever and the language model.

    :param retriever: the retriever
    :param llm: the language model
    :return: the chain
    """
    # Rag prompt
    template = """Answer the question based ONLY on the following context:
    {context}
    Question: {question}
    """
    prompt = ChatPromptTemplate.from_template(template)

    chain = ({"context": retriever, "question": RunnablePassthrough()} | prompt| llm | StrOutputParser())
    logging.info("Chain created...")
    return chain

def main():
    # Load the PDF file
    # data = ingest_pdf(DOC_PATH)

    # Load the PDF files from folder
    # data = ingest_pdf(DOC_FOLDER, folder=True)
    # web_scrap_obj = WebscrapOnlineResearch()
    
    # data_pool = list()
    data_well = list()
    index_data_pool, index_links = ingest_pdf(DOC_FOLDER, folder=True)
    res_data_pool, links = ingest_pdf(RES_FOLDER, folder=True)
    # data.append(Document(page_content=res_data_pool))
    data_well = index_data_pool + res_data_pool
    # Convert your string into Document objects
    # documents = [Document(page_content="This is the first document."),
    #             Document(page_content="This is the second document.")]

    if not (index_data_pool and res_data_pool):
        return

    if index_links:
        document_pool = list()
        # links = ["https://conbio.onlinelibrary.wiley.com/doi/10.1111/csp2.13096", "https://www.sciencedirect.com/science/article/pii/S2351989424002208?via%3Dihub"]
        for link in index_links[:2]:
            data = ingest_pdf(link, folder=False)
            if data and isinstance(data, str):
                document_pool.append(Document(page_content=data))
            else:
                # logging.error("Data is empty or not a valid string!")
                logging.error("Data is empty or not a valid string!")
            # document_pool.append(Document(page_content=data))
            # data_pool.append(data)
        data_well = data_well + document_pool
        
        

    # Split the documents
    chunks = split_documents(data_well)

    # Create a vector database
    vector_db = create_vector_db(chunks)

    # Load the language model
    llm = ChatOllama(model=MODEL)

    # Create a retriever
    retriever = create_retriever(vector_db, llm)

    # Create a chain
    chain = create_chain(retriever, llm)

    # Process user queries
    while True:
        # Ask for user input
        query = input("\n\n[Hackaholic Bot here]: How can i help you? (Type 'exit' or 'quit' or 'end' to quit): >>>> ")
        if query in ["\n", "", " "]:
            continue
        # Check if the user wants to exit
        if query.lower() in ["exit", "quit", "end"]:
            break

        # Invoke the chain to get response
        questions = [query]
        res = chain.invoke(input=(questions))
        print(f"[Hackaholic Bot's Response]: \n{res}\n\n")
        questions = []

if __name__ == "__main__":
    main()
