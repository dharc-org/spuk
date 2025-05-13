<img src="static/img/logo.png" alt="logo" width="100"/>

# SPUK (Static PUblisher of Knowledge)

## Description

SPUK is a Static Site Generator (SSG) designed for RDF Knowledge Graphs. It transforms RDF data into a browsable, static HTML website.

## Installation

1. Create a virtual environment to manage the project's dependencies:

    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:

    * On Windows:
    
        ```
        .\venv\Scripts\activate
        ```

    * On macOS and Linux:

        ```
        source venv/bin/activate
        ```

3. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

SPUK generates static HTML pages from an RDF Knowledge Graph (KG), allowing users to explore the data through a web browser.

### Start the site and the API

If you are launching the code for the first time, before running the main script, make it executable:

    chmod +x main.sh

Start the static site generator and API server:

    ./main.sh

The website will be available at: http://127.0.0.1:8001.

## Author

Barzaghi, Sebastian (https://orcid.org/0000-0002-0799-1527).