from langchain_community.document_loaders import UnstructuredExcelLoader

def excel_loader(file_path):
    loader = UnstructuredExcelLoader(file_path)
    docs = loader.load()
    print(docs[0].page_content[:300])   

excel_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\dataset.xlsx")