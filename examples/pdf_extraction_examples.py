#!/usr/bin/env python3
"""
MarkItDown PDF Extraction Examples

This script demonstrates various ways to extract text and content from PDF files
using MarkItDown. It covers basic extraction, error handling, and advanced scenarios.

Prerequisites:
    pip install 'markitdown[pdf]'  # For basic PDF support
    # OR
    pip install 'markitdown[all]'  # For all format support including Azure Document Intelligence
"""

import os
import sys
from pathlib import Path
from markitdown import MarkItDown, MissingDependencyException, UnsupportedFormatException


def basic_pdf_extraction(pdf_path):
    """
    Basic PDF text extraction example.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Extracted text content
    """
    print(f"📄 Extracting text from: {pdf_path}")
    
    try:
        # Initialize MarkItDown
        md = MarkItDown()
        
        # Convert PDF to markdown
        result = md.convert(pdf_path)
        
        # Print basic information about the result
        print(f"✅ Extraction successful!")
        print(f"📝 Content length: {len(result.text_content)} characters")
        
        if result.title:
            print(f"📋 Document title: {result.title}")
        
        return result.text_content
        
    except MissingDependencyException as e:
        print(f"❌ Missing dependencies: {e}")
        print("💡 Install PDF dependencies with: pip install 'markitdown[pdf]'")
        return None
        
    except UnsupportedFormatException as e:
        print(f"❌ Unsupported format: {e}")
        return None
        
    except Exception as e:
        print(f"❌ Extraction failed: {e}")
        return None


def save_extracted_text(pdf_path, output_path=None):
    """
    Extract PDF text and save to a markdown file.
    
    Args:
        pdf_path (str): Path to the PDF file
        output_path (str, optional): Output file path. If None, auto-generates based on PDF name.
    """
    if output_path is None:
        # Auto-generate output filename
        pdf_name = Path(pdf_path).stem
        output_path = f"{pdf_name}_extracted.md"
    
    print(f"💾 Saving extracted content to: {output_path}")
    
    try:
        md = MarkItDown()
        result = md.convert(pdf_path)
        
        # Save markdown content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(result.markdown)
        
        print(f"✅ Content saved successfully to {output_path}")
        print(f"📊 File size: {os.path.getsize(output_path)} bytes")
        
    except Exception as e:
        print(f"❌ Failed to save content: {e}")


def extract_with_azure_document_intelligence(pdf_path, endpoint):
    """
    Extract PDF using Azure Document Intelligence for better OCR and structure detection.
    
    Args:
        pdf_path (str): Path to the PDF file
        endpoint (str): Azure Document Intelligence endpoint URL
    """
    print(f"🔍 Extracting with Azure Document Intelligence from: {pdf_path}")
    
    try:
        # Initialize MarkItDown with Document Intelligence
        md = MarkItDown(docintel_endpoint=endpoint)
        result = md.convert(pdf_path)
        
        print(f"✅ Advanced extraction successful!")
        print(f"📝 Content length: {len(result.text_content)} characters")
        
        return result.text_content
        
    except Exception as e:
        print(f"❌ Azure Document Intelligence extraction failed: {e}")
        print("💡 Make sure your Azure Document Intelligence endpoint is correctly configured")
        return None


def batch_pdf_extraction(pdf_directory):
    """
    Extract text from all PDF files in a directory.
    
    Args:
        pdf_directory (str): Path to directory containing PDF files
    """
    pdf_dir = Path(pdf_directory)
    
    if not pdf_dir.exists() or not pdf_dir.is_dir():
        print(f"❌ Directory does not exist: {pdf_directory}")
        return
    
    # Find all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        print(f"📂 No PDF files found in: {pdf_directory}")
        return
    
    print(f"🔍 Found {len(pdf_files)} PDF files to process")
    
    md = MarkItDown()
    successful_extractions = 0
    
    for pdf_file in pdf_files:
        print(f"\n📄 Processing: {pdf_file.name}")
        
        try:
            result = md.convert(str(pdf_file))
            
            # Save extracted content
            output_file = pdf_file.with_suffix('.md')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(result.markdown)
            
            print(f"✅ Saved to: {output_file}")
            successful_extractions += 1
            
        except Exception as e:
            print(f"❌ Failed to process {pdf_file.name}: {e}")
    
    print(f"\n📊 Batch processing complete: {successful_extractions}/{len(pdf_files)} successful")


def preview_extraction(pdf_path, preview_length=500):
    """
    Extract and preview the first portion of PDF content.
    
    Args:
        pdf_path (str): Path to the PDF file
        preview_length (int): Number of characters to preview
    """
    print(f"👀 Previewing content from: {pdf_path}")
    
    try:
        md = MarkItDown()
        result = md.convert(pdf_path)
        
        # Show preview
        preview_text = result.text_content[:preview_length]
        print(f"\n📝 Content Preview ({preview_length} characters):")
        print("=" * 50)
        print(preview_text)
        if len(result.text_content) > preview_length:
            print(f"\n... ({len(result.text_content) - preview_length} more characters)")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Preview failed: {e}")


def main():
    """Main function with example usage."""
    print("🚀 MarkItDown PDF Extraction Examples")
    print("=" * 40)
    
    # Example PDF path - you can change this to your PDF file
    example_pdf = "example.pdf"
    
    # Check if example PDF exists
    if not os.path.exists(example_pdf):
        print(f"⚠️  Example PDF not found: {example_pdf}")
        print("\n💡 To run these examples:")
        print("1. Place a PDF file named 'example.pdf' in this directory")
        print("2. Or modify the 'example_pdf' variable to point to your PDF")
        print("3. Run this script again")
        print("\n📚 Available functions you can use:")
        print("- basic_pdf_extraction(pdf_path)")
        print("- save_extracted_text(pdf_path, output_path)")
        print("- preview_extraction(pdf_path)")
        print("- batch_pdf_extraction(directory_path)")
        print("- extract_with_azure_document_intelligence(pdf_path, endpoint)")
        return
    
    # Run examples
    print("\n1️⃣ Basic PDF Extraction:")
    text_content = basic_pdf_extraction(example_pdf)
    
    if text_content:
        print("\n2️⃣ Preview Extraction:")
        preview_extraction(example_pdf)
        
        print("\n3️⃣ Save to File:")
        save_extracted_text(example_pdf)
    
    print("\n4️⃣ Batch Processing Example:")
    print("   batch_pdf_extraction('path/to/pdf/directory')")
    
    print("\n5️⃣ Azure Document Intelligence Example:")
    print("   extract_with_azure_document_intelligence('path/to/pdf', 'https://your-endpoint.com')")
    
    print("\n✨ Examples completed! Check the generated .md files for extracted content.")


if __name__ == "__main__":
    main()