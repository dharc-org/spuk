from jinja2 import Environment, FileSystemLoader
from src.utils import escape_html, uri_to_filename, get_uri_label
import os

env = Environment(loader=FileSystemLoader("static/templates"))

class HTMLPage:
    def __init__(self, subject, property_object_pairs):
        """Initializes the HTMLPage with subject and its properties."""
        self.subject = subject
        self.property_object_pairs = property_object_pairs

    def render(self):
        """Generates the HTML for the entity subject."""
        template = env.get_template("entity.html")
        return template.render(
            subject_uri = self.subject,
            subject_label = self.subject,
            property_object_pairs = self.property_object_pairs
        )

    def save(self, output_dir="docs"):
        """Saves the HTML page to the output directory."""
        html = self.render()
        filename = uri_to_filename(self.subject)
        output_path = f"{output_dir}/{filename}.html"
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "w") as f:
            f.write(html)


class IndexPage:
    def __init__(self, entities, summary):
        """Initializes the IndexPage with the list of entities."""
        self.entities = entities
        self.summary = summary

    def render(self):
        """Generates the HTML for the index page."""
        template = env.get_template("index.html")
        items = [
            {
                "label": entity_uri,
                "filename": uri_to_filename(entity_uri),
                "type": next(
                    (prop["object_label"] for prop in props if prop["is_type"]), None
                ),
                "type_uri": next(
                    (prop["object_uri"] for prop in props if prop["is_type"]), None
                )
            }
            for entity_uri, props in self.entities.items()
        ]
        return template.render(entities=items, summary=self.summary)

    def save(self, output_dir="docs"):
        """Saves the index HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "index.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved index page to {output_dir}/index.html")


class QueryPage:
    def __init__(self, source):
        self.source = source

    def render(self):
        """Generates the HTML for the query page."""
        template = env.get_template("sparql.html")
        return template.render(source=self.source)

    def save(self, output_dir="docs"):
        """Saves the query HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "sparql.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved query page to {output_dir}/sparql.html")


class DocPage:
    def __init__(self, source):
        self.source = source

    def render(self):
        """Generates the HTML for the documentation page."""
        template = env.get_template("documentation.html")
        return template.render(source=self.source)

    def save(self, output_dir="docs"):
        """Saves the documentation HTML page."""
        os.makedirs(output_dir, exist_ok=True)
        with open(os.path.join(output_dir, "documentation.html"), "w") as f:
            f.write(self.render())
        print(f"✅ Saved query page to {output_dir}/documentation.html")