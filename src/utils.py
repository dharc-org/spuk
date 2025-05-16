import html, os
from urllib.parse import urlparse


def get_uri_label(uri: str) -> str:
    """Extracts the last fragment or path segment of a URI."""
    if "#" in uri:
        return uri.split("#")[-1]
    return uri.rstrip("/").split("/")[-1]

def escape_html(text: str) -> str:
    """Escape special characters in text for safe HTML output."""
    return html.escape(text)

def uri_to_filename(uri: str) -> str:
    """Convert a URI into a valid HTML filename."""
    path = urlparse(uri).path
    path = path.replace("#", "/")
    filename = path.strip("/").split("/")[-1]
    return filename

def get_namespace(uri: str) -> str:
    if "#" in uri:
        return uri.rsplit("#", 1)[0] + "#"
    else:
        return uri.rsplit("/", 1)[0] + "/"

def remove_root(path):
    return "/" + "/".join(path.split("/")[1:])

def generate_path(uri):
    root = "docs"
    path = urlparse(uri).path
    parts = path.strip("/").split("/")
    full_path = os.path.join(root, *parts)
    return full_path

def generate_base_path(path):
    relative_path = os.path.relpath("spuk", path)
    depth = len(relative_path.split(os.sep))
    if relative_path == ".":
        return ""
    return "../" * depth