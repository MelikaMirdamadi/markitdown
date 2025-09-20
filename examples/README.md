# MarkItDown Examples

This directory contains practical examples demonstrating how to use MarkItDown for various document conversion tasks.

## PDF Extraction Examples

**File:** `pdf_extraction_examples.py`

A comprehensive script showing different ways to extract text from PDF files:

- Basic PDF text extraction
- Saving extracted content to markdown files
- Batch processing multiple PDFs
- Using Azure Document Intelligence for better OCR
- Preview extraction with error handling

### Running the Examples

1. **Install MarkItDown with PDF support:**
   ```bash
   pip install 'markitdown[pdf]'
   ```

2. **Run the example script:**
   ```bash
   python pdf_extraction_examples.py
   ```

3. **Or use individual functions:**
   ```python
   from pdf_extraction_examples import basic_pdf_extraction
   
   text = basic_pdf_extraction("your-document.pdf")
   print(text)
   ```

### Functions Available

- `basic_pdf_extraction(pdf_path)` - Extract text from a PDF file
- `save_extracted_text(pdf_path, output_path)` - Extract and save to markdown file
- `preview_extraction(pdf_path, preview_length)` - Preview first portion of extracted text
- `batch_pdf_extraction(pdf_directory)` - Process all PDFs in a directory
- `extract_with_azure_document_intelligence(pdf_path, endpoint)` - Use Azure for better extraction

### Example Output

When you run the script with a PDF file, you'll see:

```
🚀 MarkItDown PDF Extraction Examples
========================================

1️⃣ Basic PDF Extraction:
📄 Extracting text from: example.pdf
✅ Extraction successful!
📝 Content length: 5194 characters

2️⃣ Preview Extraction:
👀 Previewing content from: example.pdf
📝 Content Preview (500 characters):
==================================================
[Content preview shown here]
==================================================

3️⃣ Save to File:
💾 Saving extracted content to: example_extracted.md
✅ Content saved successfully to example_extracted.md
📊 File size: 5200 bytes
```

## Adding Your Own Examples

Feel free to add more example scripts for other document types or use cases:

- Word document extraction
- PowerPoint presentation conversion
- Excel spreadsheet processing
- Batch processing workflows
- Integration with other tools

## Need Help?

If you encounter issues:

1. Make sure you have the right dependencies: `pip install 'markitdown[pdf]'`
2. Check that your PDF file exists and is readable
3. For scanned PDFs, consider using Azure Document Intelligence
4. See the main README.md for more troubleshooting tips