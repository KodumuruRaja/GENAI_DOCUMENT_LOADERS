import warnings
warnings.filterwarnings("ignore",category = DeprecationWarning)

from langchain_community.document_loaders import PyPDFLoader

def pdf_loader(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()
    print(data[0].page_content)
    print(len(data))

pdf_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Raja_Kodumuru_Resume_Updated.pdf")