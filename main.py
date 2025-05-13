from src.rdf_graph import RDFGraph
from src.html_page import HTMLPage, IndexPage, QueryPage, DocPage

def main():
    source = "https://chad-kg.duckdns.org/chadkg/sparql"
    rdf = RDFGraph(source, is_sparql_endpoint=True)
    entities = rdf.get_property_object_data()
    summary = rdf.get_summary()

    for entity, property_object_pairs in entities.items():
        page = HTMLPage(entity, property_object_pairs)
        page.save()

    index_page = IndexPage(entities, summary)
    index_page.save()

    sparql_page = QueryPage(source)
    sparql_page.save()

    documentation_page = DocPage(source)
    documentation_page.save()

    print("🎉 All pages generated successfully!")

if __name__ == "__main__":
    main()
