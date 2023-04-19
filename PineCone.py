
import pinecone
import pandas as pd
import numpy as np
import yaml
# use python 311
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
pinecone.init(api_key=config["Pinecone_api_key"],environment=config["environment"])
index = pinecone.Index(index_name=config["index_name"])

# def put(ids ,vectors):
#     df = pd.DataFrame(data={"id":ids ,"vector":vectors})
#     return index.upsert(vectors=zip(df.id,df.vector))
def put(ids, vectors):
    ids_arr = np.array(ids)
    arr = np.concatenate([ids_arr[:, np.newaxis], vectors], axis=1)
    vectors_list = [(str(id_), tuple(values)) for id_, *values in arr]
    return index.upsert(vectors=vectors_list)

def get(Vector):
    ndarray = np.array(Vector)

    # Convert to list
    vector = ndarray.tolist()
    res = index.query(queries=[vector],top_k=1)
    return res
# ids = []
# ids = ["a","b","c","d"]
# vector = []
# vector.append([1,2,3])
# vector.append([4,5,6])
# vector.append([7,8,9])
# vector.append([10,11,22])
# print(put(ids,vector))
# df = pd.DataFrame(
#     data={
#         "id":["a","b","c","d"],
#         "vector":[
#             [1,2,3],
#             [4,5,6],
#             [7,8,9],
#             [10,11,22]
#         ]
#     }
# )
# print(put(["a","b","c","d"],[[1,2,3], [4,5,6],  [7,8,9],  [10,11,22] ]))
#
# # pinecone.delete_index("mounirindex")


