from langchain_community.document_loaders import UnstructuredMarkdownLoader

def markdown_loader(file_path):
    loader = UnstructuredMarkdownLoader(file_path)
    docs = loader.load()
    print(docs[0].page_content[:300])

markdown_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Markdown_loader.py")