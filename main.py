import collection
import inverted_idx
from vector_model import VectorModel

from matplotlib import pyplot as plt
from sklearn.metrics import auc

query_list = [
    {
        "class": "alt.atheism",
        "query": "Atheism contradiction atheist paraphernalia moral choices independently"
    },
    {
        "class": "comp.graphics",
        "query": "plot colors image Polygon rendering"
    },
    {
        "class": "comp.sys.ibm.pc.hardware",
        "query": "subsystem Logitech Microsoft Windows Floppy"
    },
    {
        "class": "comp.windows.x",
        "query": "XFree86 Vue Xt"
    },
    {
        "class": "misc.forsale",
        "query": "FISHERMAN sale $650 HUMMINGBIRD"
    },
    {
        "class": "rec.motorcycles",
        "query": "windscreen shields K75RT BMW rec.motorcycles"
    },
    {
        "class": "sci.electronics",
        "query": "Tesla circuit volt EMI Science AC power generators"
    },
    {
        "class": "sci.med",
        "query": "OTC preparations for muscle aches"
    },
    {
        "class": "soc.religion.christian",
        "query": "even PAGAN fanaticism theology that now WORSHIPS such GODS"
    }
]

if __name__ == "__main__":
    doc_map, class_map = collection.read_all_files()
    # inv_idx, terms_in_doc = inverted_idx.gen_inverted_idx(
    #     doc_map)
    precision = []
    recall = []
    model = VectorModel(doc_map, class_map)
    avg_prec_arr = []
    for item in query_list:
        relevant_docs = 0
        res = model.retrieve(item["query"])
        # print(res)
        res_rel = []
        for tup in res:
            is_rel = False
            for term in model.terms_in_doc[tup[0]]:
                if (item["class"] in model.inverted_idx[term].classes):
                    relevant_docs += 1
                    is_rel = True
                    break
            if (is_rel):
                res_rel.append(1)
            else:
                res_rel.append(0)

        # print(res_rel)
        # print(relevant_docs)
        cur_rel = 0
        doc_num = 0
        prec_reca = [(0.0, 0.0)]
        for tup in res:
            doc_num += 1
            cur_rel += res_rel[doc_num-1]
            precision.append(cur_rel/doc_num)
            recall.append(cur_rel/relevant_docs)
            if (res_rel[doc_num-1] == 1):
                prec_reca.append((cur_rel/relevant_docs, cur_rel/doc_num))
                # prec_reca.append((cur_rel/doc_num, cur_rel/relevant_docs))
        # print("precision: ", precision)
        # print("recall: ", recall)
        average_precision = auc(*zip(*prec_reca))
        avg_prec_arr.append(average_precision)
        plt.plot(*zip(*prec_reca))
        plt.title(f'Query: "{item["query"]}"')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.figtext(0.99, 0.01, 'Average precision = %0.2f' %
                    average_precision, horizontalalignment='right')
        plt.ylim(0.0, 1.0)
        plt.xlim(0.0, 1.0)
        plt.savefig("./images/" + item['class'] + '.png')
        plt.clf()

    print("MAP = %0.2f" % (sum(avg_prec_arr / len(avg_prec_arr)))
