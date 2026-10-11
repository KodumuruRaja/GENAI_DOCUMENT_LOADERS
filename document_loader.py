from langchain_community.document_loaders import Docx2txtLoader

def docx_loader(file_path):
    loader = Docx2txtLoader(file_path)
    data = loader.load()
    print(data[0].page_content)
    print(data[0].metadata)

docx_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Bose.docx")