import math
import pandas as pd
from numpy import dot
from numpy.linalg import norm
import numpy as np
import os
import json
from nltk.tokenize import TreebankWordTokenizer
from YTMT.models import *
from sklearn.metrics.pairwise import cosine_similarity
import threading

food = []
for menu in Menu.objects.all():
    food.append(menu.name)

def update():
    user_list = []
    try:
        for user in User.objects.all():
            user_list.append(user.username)

        df = pd.DataFrame(0, columns = food, index = user_list)
        like_list = History.objects.filter(user_id = user)
        for like in like_list:
            df.loc[name, like.menu.name] = 1
    except:
        pass

    similarities = cosine_similarity(df)
    sim_df=pd.DataFrame(similarities, columns = user_list, index = user_list)
    sim_df.to_csv("collaborative_matrix.csv", mode='w', encoding='utf-8-sig')

    threading.Timer(5, update).start()
    print("update start")


if __name__ == '__main__':
    update()