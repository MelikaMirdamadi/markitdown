# MarkItDown

[![PyPI](https://img.shields.io/pypi/v/markitdown.svg)](https://pypi.org/project/markitdown/)
![PyPI - Downloads](https://img.shields.io/pypi/dd/markitdown)
[![Built by AutoGen Team](https://img.shields.io/badge/Built%20by-AutoGen%20Team-blue)](https://github.com/microsoft/autogen)

> [!TIP]
> MarkItDown now offers an MCP (Model Context Protocol) server for integration with LLM applications like Claude Desktop. See [markitdown-mcp](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp) for more information.

> [!IMPORTANT]
> Breaking changes between 0.0.1 to 0.1.0:
> * Dependencies are now organized into optional feature-groups (further details below). Use `pip install 'markitdown[all]'` to have backward-compatible behavior. 
> * convert\_stream() now requires a binary file-like object (e.g., a file opened in binary mode, or an io.BytesIO object). This is a breaking change from the previous version, where it previously also accepted text file-like objects, like io.StringIO.
> * The DocumentConverter class interface has changed to read from file-like streams rather than file paths. *No temporary files are created anymore*. If you are the maintainer of a plugin, or custom DocumentConverter, you likely need to update your code. Otherwise, if only using the MarkItDown class or CLI (as in these examples), you should not need to change anything.

MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines. To this end, it is most comparable to [textract](https://github.com/deanmalmgren/textract), but with a focus on preserving important document structure and content as Markdown (including: headings, lists, tables, links, etc.) While the output is often reasonably presentable and human-friendly, it is meant to be consumed by text analysis tools -- and may not be the best option for high-fidelity document conversions for human consumption.

MarkItDown currently supports the conversion from:

- PDF
- PowerPoint
- Word
- Excel
- Images (EXIF metadata and OCR)
- Audio (EXIF metadata and speech transcription)
- HTML
- Text-based formats (CSV, JSON, XML)
- ZIP files (iterates over contents)
- Youtube URLs
- EPubs
- ... and more!

## Quick Start: PDF Extraction

**Want to extract text from your PDF? Here's how:**

### 1. Install MarkItDown
```bash
# Install with PDF support
pip install 'markitdown[pdf]'

# Or install with all format support
pip install 'markitdown[all]'
```

### 2. Extract PDF Content

**Command Line:**
```bash
# Convert PDF to markdown and display in terminal
markitdown your-document.pdf

# Save to a markdown file
markitdown your-document.pdf -o extracted-text.md

# Or using output redirection
markitdown your-document.pdf > extracted-text.md
```

**Python Code:**
```python
from markitdown import MarkItDown

# Initialize the converter
md = MarkItDown()

# Convert PDF to markdown
result = md.convert("your-document.pdf")

# Get the extracted text
text_content = result.text_content
print(text_content)

# Or get the markdown with formatting
markdown_content = result.markdown
print(markdown_content)
```

**Docker:**
```bash
# Build the Docker image
docker build -t markitdown:latest .

# Convert PDF using Docker
docker run --rm -i markitdown:latest < your-document.pdf > extracted-text.md
```

### 3. Advanced PDF Options

For better PDF extraction with Azure Document Intelligence:
```bash
# Using Azure Document Intelligence (requires Azure setup)
markitdown your-document.pdf -d -e "<your-document-intelligence-endpoint>"
```

```python
# Python with Azure Document Intelligence
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<your-document-intelligence-endpoint>")
result = md.convert("your-document.pdf")
print(result.text_content)
```

### Troubleshooting PDF Extraction

- **Missing dependencies error?** Install PDF dependencies with `pip install 'markitdown[pdf]'`
- **Low-quality extraction?** Try Azure Document Intelligence for better OCR and structure recognition
- **Large PDFs?** The extraction preserves text content but simplifies formatting for LLM consumption
- **Scanned PDFs?** Consider using Azure Document Intelligence which includes OCR capabilities

## Why Markdown?

Markdown is extremely close to plain text, with minimal markup or formatting, but still
provides a way to represent important document structure. Mainstream LLMs, such as
OpenAI's GPT-4o, natively "_speak_" Markdown, and often incorporate Markdown into their
responses unprompted. This suggests that they have been trained on vast amounts of
Markdown-formatted text, and understand it well. As a side benefit, Markdown conventions
are also highly token-efficient.

## Prerequisites
MarkItDown requires Python 3.10 or higher. It is recommended to use a virtual environment to avoid dependency conflicts.

With the standard Python installation, you can create and activate a virtual environment using the following commands:

```bash
python -m venv .venv
source .venv/bin/activate
```

If using `uv`, you can create a virtual environment with:

```bash
uv venv --python=3.12 .venv
source .venv/bin/activate
# NOTE: Be sure to use 'uv pip install' rather than just 'pip install' to install packages in this virtual environment
```

If you are using Anaconda, you can create a virtual environment with:

```bash
conda create -n markitdown python=3.12
conda activate markitdown
```

## Installation

To install MarkItDown, use pip: `pip install 'markitdown[all]'`. Alternatively, you can install it from the source:

```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
```

## Usage

### Command-Line

```bash
markitdown path-to-file.pdf > document.md
```

Or use `-o` to specify the output file:

```bash
markitdown path-to-file.pdf -o document.md
```

You can also pipe content:

```bash
cat path-to-file.pdf | markitdown
```

### Optional Dependencies
MarkItDown has optional dependencies for activating various file formats. Earlier in this document, we installed all optional dependencies with the `[all]` option. However, you can also install them individually for more control. For example:

```bash
pip install 'markitdown[pdf, docx, pptx]'
```

will install only the dependencies for PDF, DOCX, and PPTX files.

At the moment, the following optional dependencies are available:

* `[all]` Installs all optional dependencies
* `[pptx]` Installs dependencies for PowerPoint files
* `[docx]` Installs dependencies for Word files
* `[xlsx]` Installs dependencies for Excel files
* `[xls]` Installs dependencies for older Excel files
* `[pdf]` Installs dependencies for PDF files
* `[outlook]` Installs dependencies for Outlook messages
* `[az-doc-intel]` Installs dependencies for Azure Document Intelligence
* `[audio-transcription]` Installs dependencies for audio transcription of wav and mp3 files
* `[youtube-transcription]` Installs dependencies for fetching YouTube video transcription

### Plugins

MarkItDown also supports 3rd-party plugins. Plugins are disabled by default. To list installed plugins:

```bash
markitdown --list-plugins
```

To enable plugins use:

```bash
markitdown --use-plugins path-to-file.pdf
```

To find available plugins, search GitHub for the hashtag `#markitdown-plugin`. To develop a plugin, see `packages/markitdown-sample-plugin`.

### Azure Document Intelligence

To use Microsoft Document Intelligence for conversion:

```bash
markitdown path-to-file.pdf -o document.md -d -e "<document_intelligence_endpoint>"
```

More information about how to set up an Azure Document Intelligence Resource can be found [here](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/how-to-guides/create-document-intelligence-resource?view=doc-intel-4.0.0)

### Python API

Basic usage in Python:

```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("test.xlsx")
print(result.text_content)
```

Document Intelligence conversion in Python:

```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
result = md.convert("test.pdf")
print(result.text_content)
```

To use Large Language Models for image descriptions (currently only for pptx and image files), provide `llm_client` and `llm_model`:

```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o", llm_prompt="optional custom prompt")
result = md.convert("example.jpg")
print(result.text_content)
```

### More Examples

📂 **Check out the [examples directory](examples/) for comprehensive PDF extraction examples and other use cases:**

- **[`examples/pdf_extraction_examples.py`](examples/pdf_extraction_examples.py)** - Complete PDF extraction examples with error handling, batch processing, and Azure Document Intelligence integration
- **[`examples/README.md`](examples/README.md)** - Detailed guide for running the examples

The examples include:
- Basic PDF text extraction
- Saving to markdown files
- Batch processing multiple PDFs
- Preview extraction
- Advanced extraction with Azure Document Intelligence

### Docker

```sh
docker build -t markitdown:latest .
docker run --rm -i markitdown:latest < ~/your-file.pdf > output.md
```

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

### How to Contribute

You can help by looking at issues or helping review PRs. Any issue or PR is welcome, but we have also marked some as 'open for contribution' and 'open for reviewing' to help facilitate community contributions. These are of course just suggestions and you are welcome to contribute in any way you like.

<div align="center">

|            | All                                                          | Especially Needs Help from Community                                                                                                      |
| ---------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Issues** | [All Issues](https://github.com/microsoft/markitdown/issues) | [Issues open for contribution](https://github.com/microsoft/markitdown/issues?q=is%3Aissue+is%3Aopen+label%3A%22open+for+contribution%22) |
| **PRs**    | [All PRs](https://github.com/microsoft/markitdown/pulls)     | [PRs open for reviewing](https://github.com/microsoft/markitdown/pulls?q=is%3Apr+is%3Aopen+label%3A%22open+for+reviewing%22)              |

</div>

### Running Tests and Checks

- Navigate to the MarkItDown package:

  ```sh
  cd packages/markitdown
  ```

- Install `hatch` in your environment and run tests:

  ```sh
  pip install hatch  # Other ways of installing hatch: https://hatch.pypa.io/dev/install/
  hatch shell
  hatch test
  ```

  (Alternative) Use the Devcontainer which has all the dependencies installed:

  ```sh
  # Reopen the project in Devcontainer and run:
  hatch test
  ```

- Run pre-commit checks before submitting a PR: `pre-commit run --all-files`

### Contributing 3rd-party Plugins

You can also contribute by creating and sharing 3rd party plugins. See `packages/markitdown-sample-plugin` for more details.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
