# Eagle API Documentation (LLM-Friendly)  

This repository provides a structured and LLM-friendly version of the [Eagle API documentation](https://developer.eagle.cool/plugin-api).  

> **Note**: The contents are scraped from the official API webpage. I do not own the rights to this documentation.  

## 📌 Usage  

- Copy the contents of **[repomix-output.md](repomix-output.md)** directly into an LLM.  
- Alternatively, view individual API pages in the `./plugin-api/` folder.  

## 🔧 How to Build the Documentation  

### 1. Extract `index.md`  
- Navigate to any page on the official API docs site.  
- Use `markitdown` to extract the index.  
- Save the extracted content as `index.md`.  

### 2. Scrape a New Version of the Docs  
- Run the `scrape_docs.ipynb` notebook in the `src/` folder.  

### 3. Generate an LLM-Friendly Version  
- Use `repomix` to format the documentation for better LLM compatibility:  

```bash
# Install repomix if not already installed
pip install repomix

# Navigate to the docs directory and run repomix
cd docs/
python -m repomix
```