from langchain_community.document_loaders import WebBaseLoader

def web_loader(url):
    loader = WebBaseLoader(url)
    data = loader.load()
    print(data[0].page_content)
    print(data[0].metadata)

web_loader("https://en.wikipedia.org/wiki/Artificial_intelligence")