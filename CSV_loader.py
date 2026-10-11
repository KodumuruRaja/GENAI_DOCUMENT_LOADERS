import warnings
warnings.filterwarnings("ignore",category = DeprecationWarning)

from langchain_community.document_loaders import CSVLoader

def csv_loader(file_path):
    loader = CSVLoader(file_path)
    data = loader.load()
    print(data[0].page_content)

csv_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\AggregatedData.csv")