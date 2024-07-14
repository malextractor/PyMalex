import sys
from os import path

sys.path.insert(0, path.abspath(path.join(path.dirname(__file__), '..')))

from pymalex import PyMalex, MalexSources

def main():
    pymalex_instance = PyMalex("http://localhost:5000", "key", debug=True)
    
    sources_handler = MalexSources(pymalex_instance)

    print("Liste des sources:")
    sources_list = sources_handler.list_sources()
    print(sources_list)

    new_source_data = {
        "name": "Private Source",
        "url": "http://private.source",
        "filter": "oui"
    }
    print("\nAjout d'une nouvelle source:")
    new_source = sources_handler.add_source(new_source_data)
    print(new_source)

    source_id_to_modify = "4"
    updated_source_data = {
        "name": "Updated Name",
        "url": "http://updated.source"
    }
    print("\nModification d'une source:")
    modified_source = sources_handler.modify_source(source_id_to_modify, updated_source_data)
    print(modified_source)

    source_id_to_delete = "5"
    print("\nSuppression d'une source:")
    deleted_source = sources_handler.delete_source(source_id_to_delete)
    print(deleted_source)

if __name__ == "__main__":
    main()
