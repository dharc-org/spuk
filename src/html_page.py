from jinja2 import Environment, FileSystemLoader
from src.utils import escape_html, uri_to_filename, get_uri_label, remove_root, generate_base_path, generate_path
from rdflib import Graph, URIRef, Literal, RDF
from urllib.parse import urlparse
import os

env = Environment(loader=FileSystemLoader("static/templates"))

class HTMLPage:
    def __init__(self, subject, property_object_pairs, source):
        """Initializes the HTMLPage with subject and its properties."""
        self.subject = subject
        self.type = None
        self.property_object_pairs = property_object_pairs
        self.source = source
        self.path = generate_path(self.subject)
        self.rdf = self.generate_rdf()
        self.base_path = generate_base_path(self.get_path())

    def render(self):
        """Generates the HTML for the entity subject."""
        template = env.get_template("entity.html")
        return template.render(
            subject_uri = self.subject,
            subject_label = self.subject,
            property_object_pairs = self.property_object_pairs,
            base_path = self.base_path,
            #path = f"{remove_root(self.get_path())}/{uri_to_filename(self.subject)}"
            path = f"{self.get_path()}/{uri_to_filename(self.subject)}"
        )

    def save(self):
        """Saves the HTML page to the output directory."""
        html = self.render()
        output_path = os.path.join(self.get_path(), f"{uri_to_filename(self.subject)}.html")
        with open(output_path, "w") as f:
            f.write(html)

    def generate_path(self):
        root = "docs"
        path = urlparse(self.subject).path
        parts = path.strip("/").split("/")
        full_path = os.path.join(root, *parts)
        return full_path

    def get_path(self):
        return self.path

    def generate_folders(self):
        os.makedirs(self.get_path())

    def generate_rdf(self):
        source = self.source.graph
        g = Graph()
        for prefix, namespace in source.namespaces():
            g.bind(prefix, namespace)
        for s, p, o in source.triples((URIRef(self.subject), None, None)):
            g.add((s, p, o))
            if p == RDF.type:
                self.type = str(p)
        return g
    
    def get_rdf(self):
        return self.rdf
    
    def get_type(self):
        return self.type

    def serialize(self):
        formats = {
            "turtle": "ttl",
            "nt": "nt",
            "xml": "xml",
            "json-ld": "jsonld"
        }
        for frmt, ext in formats.items():
            rdf = self.get_rdf()
            filename = uri_to_filename(self.subject)
            full_path = os.path.join(self.get_path(), f"{filename}.{ext}")
            rdf.serialize(
                destination=full_path, 
                format=frmt,
                encoding="utf-8"
            )



class IndexPage:
    def __init__(self, entities, summary):
        """Initializes the IndexPage with the list of entities."""
        self.entities = entities
        self.summary = summary
        self.base_path = generate_base_path("")

    def render(self):
        """Generates the HTML for the index page."""
        template = env.get_template("index.html")
        items = [
            {
                "uri": entity.subject,
                #"path": f"{remove_root(entity.get_path())}/{uri_to_filename(entity.subject)}",
                "path": f"{entity.get_path()}/{uri_to_filename(entity.subject)}",
                "type": uri_to_filename(entity.get_type()),
                "type_uri": entity.get_type()
            }
            for entity in self.entities
        ]
        return template.render(
            entities = items, 
            summary = self.summary,
            base_path = self.base_path
        )

    def save(self, output_dir="docs"):
        """Saves the index HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "index.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved index page to {output_dir}/index.html")


class QueryPage:
    def __init__(self, source):
        self.source = source
        self.base_path = generate_base_path("")

    def render(self):
        """Generates the HTML for the query page."""
        template = env.get_template("sparql.html")
        return template.render(
            source = self.source,
            base_path = self.base_path
        )

    def save(self, output_dir="docs"):
        """Saves the query HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "sparql.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved query page to {output_dir}/sparql.html")


class DocPage:
    def __init__(self, source):
        self.source = source
        self.base_path = generate_base_path("")

    def render(self):
        """Generates the HTML for the documentation page."""
        template = env.get_template("documentation.html")
        return template.render(
            source = self.source,
            base_path = self.base_path
        )

    def save(self, output_dir="docs"):
        """Saves the documentation HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "documentation.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved query page to {output_dir}/documentation.html")