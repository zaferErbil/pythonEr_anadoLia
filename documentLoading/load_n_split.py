from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

PDF_PATH = "../documents/ozel_saglik_sigortasi_avantajlari.pdf"

loader = PyPDFLoader(PDF_PATH)

pages = loader.load_and_split()

# embedding function
embeddings_function = SentenceTransformerEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


vectordb = Chroma.from_documents(
    documents=pages,
    embedding=embeddings_function,
    persist_directory="../vector_db",
    collection_name="ozel_saglik_sigortasi_avantajlari"
)



vectordb.persist()