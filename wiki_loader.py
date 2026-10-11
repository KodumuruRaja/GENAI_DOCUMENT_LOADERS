import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
from langchain_community.document_loaders import WikipediaLoader

def wiki_loader(qa):
    loader = WikipediaLoader(query=qa, load_max_docs=1)
    docs = loader.load()
    print(docs[0].page_content[:300])

wiki_loader("Langchain")