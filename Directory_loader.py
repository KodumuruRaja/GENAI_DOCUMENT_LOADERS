from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    path=r"C:\Users\Megha\Desktop\Personal",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
docs = loader.load()

print(f"Loaded {len(docs)} files from directory.")
