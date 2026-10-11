import warnings
warnings.filterwarnings("ignore",category = DeprecationWarning)

from langchain_community.document_loaders import TextLoader

def text_loader(file_path, encoding):
    loader = TextLoader(file_path, encoding=encoding)
    data = loader.load()
    print(data[0].page_content)
    print(data[0].metadata)

text_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\Indian Independence Act, 1947..txt", "utf-8")



