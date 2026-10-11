from langchain_community.document_loaders import BSHTMLLoader


def html_loader(file_path):
    loader = BSHTMLLoader(file_path)
    data = loader.load()
    print(data[0].page_content)
    print(data[0].metadata)

html_loader(r"C:\Users\Megha\Desktop\GENAI_CONCEPTS\sample1.html")