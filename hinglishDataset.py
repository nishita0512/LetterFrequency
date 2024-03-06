import os
from datasets import load_dataset

dataset = load_dataset("rishiraj/hinglish", split='train')

with open('hinglish.txt', 'w', encoding="utf-8") as f:
    dtlen = len(dataset)

    for i in range(dtlen):
        m = dataset["messages"][i]
        os.system('cls')
        print("Processing: ",i, "/",dtlen)

        for d in m:
            v = d["content"]
            f.write(v + '\n')

