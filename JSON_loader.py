import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import JSONLoader

def json_loader(file_path):
    # "." extract the entire JSON contents as string content
    loader = JSONLoader(file_path, jq_schema=".", text_content=False)
    data = loader.load()
    print(data[0].page_content)

json_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\sample.json")
