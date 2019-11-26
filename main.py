import collection
import inverted_idx

if __name__ == "__main__":
    doc_map, class_map = collection.read_all_files()
    inv_idx, terms_in_doc = inverted_idx.gen_inverted_idx(
        doc_map)
