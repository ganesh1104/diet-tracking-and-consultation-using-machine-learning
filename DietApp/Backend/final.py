# type: ignore
import json
from flask import Flask, redirect, url_for, request
import json
import warnings
warnings.filterwarnings("ignore")


def Weight_Loss(e1, e3, e4, USER_INP):
    print("Weight_Loss Age : %s Years Weight: %s Kg Height: %s m mode : %s \n " %
          (e1, e3, e4, USER_INP))

    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans

    data = pd.read_csv('input.csv')

    Breakfastdata = data['Breakfast']
    BreakfastdataNumpy = Breakfastdata.to_numpy()

    Lunchdata = data['Lunch']
    LunchdataNumpy = Lunchdata.to_numpy()

    Dinnerdata = data['Dinner']
    DinnerdataNumpy = Dinnerdata.to_numpy()

    Food_itemsdata = data['Food_items']
    breakfastfoodseparated = []
    Lunchfoodseparated = []
    Dinnerfoodseparated = []

    breakfastfoodseparatedID = []
    LunchfoodseparatedID = []
    DinnerfoodseparatedID = []

    for i in range(len(Breakfastdata)):
        if BreakfastdataNumpy[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)
        if LunchdataNumpy[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)
        if DinnerdataNumpy[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    val = list(np.arange(5, 16))
    Valapnd = [0]+[4]+val
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T

    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    val = list(np.arange(5, 16))
    Valapnd = [0]+[4]+val
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T

    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T
    val = list(np.arange(5, 16))
    Valapnd = [0]+[4]+val
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T

    age = int(e1)
    weight = float(e3)
    height = float(e4)
    bmi = weight/(height**2)

    for lp in range(0, 80, 20):
        test_list = np.arange(lp, lp+20)
        for i in test_list:
            if (i == age):
                # print('age is between', str(lp), str(lp+10))
                agecl = round(lp/20)

    # print("Your body mass index is: ", bmi)
    if (bmi < 16):
        # print("severely underweight")
        clbmi = 4
    elif (bmi >= 16 and bmi < 18.5):
        # print("underweight")
        clbmi = 3
    elif (bmi >= 18.5 and bmi < 25):
        # print("Healthy")
        clbmi = 2
    elif (bmi >= 25 and bmi < 30):
        # print("overweight")
        clbmi = 1
    elif (bmi >= 30):
        # print("severely overweight")
        clbmi = 0
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.to_numpy()
    ti = (clbmi+agecl)/2

 # K-Means Based  Dinner Food
    Datacalorie = DinnerfoodseparatedIDdata[1:, 1:len(
        DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    dnrlbl = kmeans.labels_

    # K-Means Based  Lunch Food
    Datacalorie = LunchfoodseparatedIDdata[1:, 1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    lnchlbl = kmeans.labels_

    # K-Means Based  Breakfast Food
    Datacalorie = breakfastfoodseparatedIDdata[1:, 1:len(
        breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    brklbl = kmeans.labels_

    # Reading of the Dataset
    datafin = pd.read_csv('inputfin.csv')

    dataTog = datafin.T

    bmicls = [0, 1, 2, 3, 4]
    agecls = [0, 1, 2, 3, 4]

    weightlosscat = dataTog.iloc[[1, 2, 7, 8]]
    weightlosscat = weightlosscat.T
    weightgaincat = dataTog.iloc[[0, 1, 2, 3, 4, 7, 9, 10]]
    weightgaincat = weightgaincat.T
    healthycat = dataTog.iloc[[1, 2, 3, 4, 6, 7, 9]]
    healthycat = healthycat.T
    weightlosscatDdata = weightlosscat.to_numpy()
    weightgaincatDdata = weightgaincat.to_numpy()
    healthycatDdata = healthycat.to_numpy()
    weightlosscat = weightlosscatDdata[1:, 0:len(weightlosscatDdata)]
    weightgaincat = weightgaincatDdata[1:, 0:len(weightgaincatDdata)]
    healthycat = healthycatDdata[1:, 0:len(healthycatDdata)]

    weightlossfin = np.zeros((len(weightlosscat)*5, 6), dtype=np.float32)
    weightgainfin = np.zeros((len(weightgaincat)*5, 10), dtype=np.float32)
    healthycatfin = np.zeros((len(healthycat)*5, 9), dtype=np.float32)

    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    for zz in range(5):
        for jj in range(len(weightlosscat)):
            valloc = list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[t] = np.array(valloc)
            yt.append(brklbl[jj])
            t += 1

        for jj in range(len(weightlosscat)):
            valloc = list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[r] = np.array(valloc)
            yr.append(lnchlbl[jj])
            r += 1

        for jj in range(len(weightlosscat)):
            valloc = list(weightlosscat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightlossfin[s] = np.array(valloc)
            ys.append(dnrlbl[jj])
            s += 1

    X_test = np.zeros((len(weightlosscat), 6), dtype=np.float32)

    for jj in range(len(weightlosscat)):
        valloc = list(weightlosscat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj] = np.array(valloc)*ti

    from sklearn.model_selection import train_test_split

    val = int(USER_INP)

    if val == 1:
        X_train = weightlossfin
        y_train = yt

    elif val == 2:
        X_train = weightlossfin
        y_train = yr

    elif val == 3:
        X_train = weightlossfin
        y_train = ys

    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier(n_estimators=100)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    m_items = []
    for ii in range(len(y_pred)):
        if y_pred[ii] == 2:
            it = [ii, Food_itemsdata[ii]]
            v = data.loc[[ii]].to_numpy()
            it.append(v[0][5])
            it.append(v[0][6])
            it.append(v[0][6])
            it.append(v[0][7])
            it.append(v[0][12])
            it.append(v[0][15])

            m_items.append(it)

    return m_items


def Weight_Gain(e1, e3, e4, USER_INP):
    print("Weight_Gain Age : %s Years Weight: %s Kg Height: %s m mode : %s \n " %
          (e1, e3, e4, USER_INP))

    import pandas as pd
    import numpy as np
    from sklearn.cluster import KMeans

    data = pd.read_csv('input.csv')
    data.head(5)
    Breakfastdata = data['Breakfast']
    BreakfastdataNumpy = Breakfastdata.to_numpy()

    Lunchdata = data['Lunch']
    LunchdataNumpy = Lunchdata.to_numpy()

    Dinnerdata = data['Dinner']
    DinnerdataNumpy = Dinnerdata.to_numpy()

    Food_itemsdata = data['Food_items']
    breakfastfoodseparated = []
    Lunchfoodseparated = []
    Dinnerfoodseparated = []

    breakfastfoodseparatedID = []
    LunchfoodseparatedID = []
    DinnerfoodseparatedID = []

    for i in range(len(Breakfastdata)):
        if BreakfastdataNumpy[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)
        if LunchdataNumpy[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)
        if DinnerdataNumpy[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T

    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T

    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T

    age = int(e1)
    weight = float(e3)
    height = float(e4)
    bmi = weight/(height**2)
    agewiseinp = 0

    for lp in range(0, 80, 20):
        test_list = np.arange(lp, lp+20)
        for i in test_list:
            if (i == age):
                # print('age is between', str(lp), str(lp+10))
                tr = round(lp/20)
                agecl = round(lp/20)

    # print("Your body mass index is: ", bmi)
    if (bmi < 16):
        # print("severely underweight")
        clbmi = 4
    elif (bmi >= 16 and bmi < 18.5):
        # print("underweight")
        clbmi = 3
    elif (bmi >= 18.5 and bmi < 25):
        # print("Healthy")
        clbmi = 2
    elif (bmi >= 25 and bmi < 30):
        # print("overweight")
        clbmi = 1
    elif (bmi >= 30):
        # print("severely overweight")
        clbmi = 0
    val1 = DinnerfoodseparatedIDdata.describe()
    valTog = val1.T
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.to_numpy()
    ti = (bmi+agecl)/2

    # K-Means Based  Dinner Food
    Datacalorie = DinnerfoodseparatedIDdata[1:, 1:len(
        DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    dnrlbl = kmeans.labels_

    # K-Means Based  lunch Food
    Datacalorie = LunchfoodseparatedIDdata[1:, 1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    lnchlbl = kmeans.labels_

    # K-Means Based  lunch Food
    Datacalorie = breakfastfoodseparatedIDdata[1:, 1:len(
        breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    brklbl = kmeans.labels_

    inp = []
    datafin = pd.read_csv('inputfin.csv')
    datafin.head(5)
    dataTog = datafin.T
    bmicls = [0, 1, 2, 3, 4]
    agecls = [0, 1, 2, 3, 4]
    weightlosscat = dataTog.iloc[[1, 2, 7, 8]]
    weightlosscat = weightlosscat.T
    weightgaincat = dataTog.iloc[[0, 1, 2, 3, 4, 7, 9, 10]]
    weightgaincat = weightgaincat.T
    healthycat = dataTog.iloc[[1, 2, 3, 4, 6, 7, 9]]
    healthycat = healthycat.T
    weightlosscatDdata = weightlosscat.to_numpy()
    weightgaincatDdata = weightgaincat.to_numpy()
    healthycatDdata = healthycat.to_numpy()
    weightlosscat = weightlosscatDdata[1:, 0:len(weightlosscatDdata)]
    weightgaincat = weightgaincatDdata[1:, 0:len(weightgaincatDdata)]
    healthycat = healthycatDdata[1:, 0:len(healthycatDdata)]

    weightlossfin = np.zeros((len(weightlosscat)*5, 6), dtype=np.float32)
    weightgainfin = np.zeros((len(weightgaincat)*5, 10), dtype=np.float32)
    healthycatfin = np.zeros((len(healthycat)*5, 9), dtype=np.float32)
    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    for zz in range(5):
        for jj in range(len(weightgaincat)):
            valloc = list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[t] = np.array(valloc)
            yt.append(brklbl[jj])
            t += 1
        for jj in range(len(weightgaincat)):
            valloc = list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[r] = np.array(valloc)
            yr.append(lnchlbl[jj])
            r += 1
        for jj in range(len(weightgaincat)):
            valloc = list(weightgaincat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            weightgainfin[s] = np.array(valloc)
            ys.append(dnrlbl[jj])
            s += 1

    X_test = np.zeros((len(weightgaincat), 10), dtype=np.float32)

    for jj in range(len(weightgaincat)):
        valloc = list(weightgaincat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj] = np.array(valloc)*ti

    from sklearn.model_selection import train_test_split

    val = int(USER_INP)

    if val == 1:
        X_train = weightgainfin
        y_train = yt

    elif val == 2:
        X_train = weightgainfin
        y_train = yr

    elif val == 3:
        X_train = weightgainfin
        y_train = ys

    from sklearn.model_selection import train_test_split

    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier(n_estimators=100)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    m_items = []
    for ii in range(len(y_pred)):
        if y_pred[ii] == 2:
            it = [ii, Food_itemsdata[ii]]
            v = data.loc[[ii]].to_numpy()
            it.append(v[0][5])
            it.append(v[0][6])
            it.append(v[0][6])
            it.append(v[0][7])
            it.append(v[0][12])
            it.append(v[0][15])
            m_items.append(it)
    return m_items


def Healthy(e1, e3, e4, USER_INP):
    print("Healthy Age : %s Years Weight: %s Kg Height: %s m mode : %s \n " %
          (e1, e3, e4, USER_INP))

    import pandas as pd
    import numpy as np

    from sklearn.cluster import KMeans

    data = pd.read_csv('input.csv')
    data.head(5)
    Breakfastdata = data['Breakfast']
    BreakfastdataNumpy = Breakfastdata.to_numpy()

    Lunchdata = data['Lunch']
    LunchdataNumpy = Lunchdata.to_numpy()

    Dinnerdata = data['Dinner']
    DinnerdataNumpy = Dinnerdata.to_numpy()

    Food_itemsdata = data['Food_items']
    breakfastfoodseparated = []
    Lunchfoodseparated = []
    Dinnerfoodseparated = []

    breakfastfoodseparatedID = []
    LunchfoodseparatedID = []
    DinnerfoodseparatedID = []

    for i in range(len(Breakfastdata)):
        if BreakfastdataNumpy[i] == 1:
            breakfastfoodseparated.append(Food_itemsdata[i])
            breakfastfoodseparatedID.append(i)
        if LunchdataNumpy[i] == 1:
            Lunchfoodseparated.append(Food_itemsdata[i])
            LunchfoodseparatedID.append(i)
        if DinnerdataNumpy[i] == 1:
            Dinnerfoodseparated.append(Food_itemsdata[i])
            DinnerfoodseparatedID.append(i)

    LunchfoodseparatedIDdata = data.iloc[LunchfoodseparatedID]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.iloc[Valapnd]
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.T

    breakfastfoodseparatedIDdata = data.iloc[breakfastfoodseparatedID]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.iloc[Valapnd]
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.T

    DinnerfoodseparatedIDdata = data.iloc[DinnerfoodseparatedID]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T
    val = list(np.arange(5, 15))
    Valapnd = [0]+val
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.iloc[Valapnd]
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.T

    age = int(e1)
    weight = float(e3)
    height = float(e4)
    bmi = weight/(height**2)
    agewiseinp = 0

    for lp in range(0, 80, 20):
        test_list = np.arange(lp, lp+20)
        for i in test_list:
            if (i == age):
                tr = round(lp/20)
                agecl = round(lp/20)

    # print("Your body mass index is: ", bmi)
    if (bmi < 16):
        # print("severely underweight")
        clbmi = 4
    elif (bmi >= 16 and bmi < 18.5):
        # print("underweight")
        clbmi = 3
    elif (bmi >= 18.5 and bmi < 25):
        # print("Healthy")
        clbmi = 2
    elif (bmi >= 25 and bmi < 30):
        # print("overweight")
        clbmi = 1
    elif (bmi >= 30):
        # print("severely overweight")
        clbmi = 0
    val1 = DinnerfoodseparatedIDdata.describe()
    valTog = val1.T
    DinnerfoodseparatedIDdata = DinnerfoodseparatedIDdata.to_numpy()
    LunchfoodseparatedIDdata = LunchfoodseparatedIDdata.to_numpy()
    breakfastfoodseparatedIDdata = breakfastfoodseparatedIDdata.to_numpy()
    ti = (bmi+agecl)/2

    # K-Means Based  Dinner Food
    Datacalorie = DinnerfoodseparatedIDdata[1:, 1:len(
        DinnerfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    dnrlbl = kmeans.labels_

    # K-Means Based  lunch Food
    Datacalorie = LunchfoodseparatedIDdata[1:, 1:len(LunchfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    lnchlbl = kmeans.labels_

    # K-Means Based  lunch Food
    Datacalorie = breakfastfoodseparatedIDdata[1:, 1:len(
        breakfastfoodseparatedIDdata)]
    X = np.array(Datacalorie)
    kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
    XValu = np.arange(0, len(kmeans.labels_))
    brklbl = kmeans.labels_
    inp = []
    datafin = pd.read_csv('inputfin.csv')
    datafin.head(5)
    dataTog = datafin.T
    bmicls = [0, 1, 2, 3, 4]
    agecls = [0, 1, 2, 3, 4]
    weightlosscat = dataTog.iloc[[1, 2, 7, 8]]
    weightlosscat = weightlosscat.T
    weightgaincat = dataTog.iloc[[0, 1, 2, 3, 4, 7, 9, 10]]
    weightgaincat = weightgaincat.T
    healthycat = dataTog.iloc[[1, 2, 3, 4, 6, 7, 9]]
    healthycat = healthycat.T
    weightlosscatDdata = weightlosscat.to_numpy()
    weightgaincatDdata = weightgaincat.to_numpy()
    healthycatDdata = healthycat.to_numpy()
    weightlosscat = weightlosscatDdata[1:, 0:len(weightlosscatDdata)]
    weightgaincat = weightgaincatDdata[1:, 0:len(weightgaincatDdata)]
    healthycat = healthycatDdata[1:, 0:len(healthycatDdata)]

    weightlossfin = np.zeros((len(weightlosscat)*5, 6), dtype=np.float32)
    weightgainfin = np.zeros((len(weightgaincat)*5, 10), dtype=np.float32)
    healthycatfin = np.zeros((len(healthycat)*5, 9), dtype=np.float32)
    t = 0
    r = 0
    s = 0
    yt = []
    yr = []
    ys = []
    for zz in range(5):
        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[t] = np.array(valloc)
            yt.append(brklbl[jj])
            t += 1
        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[r] = np.array(valloc)
            yr.append(lnchlbl[jj])
            r += 1
        for jj in range(len(healthycat)):
            valloc = list(healthycat[jj])
            valloc.append(bmicls[zz])
            valloc.append(agecls[zz])
            healthycatfin[s] = np.array(valloc)
            ys.append(dnrlbl[jj])
            s += 1

    X_test = np.zeros((len(healthycat)*5, 9), dtype=np.float32)
    for jj in range(len(healthycat)):
        valloc = list(healthycat[jj])
        valloc.append(agecl)
        valloc.append(clbmi)
        X_test[jj] = np.array(valloc)*ti

    from sklearn.model_selection import train_test_split

    val = int(USER_INP)

    if val == 1:
        X_train = healthycatfin
        y_train = yt

    elif val == 2:
        X_train = healthycatfin
        y_train = yt

    elif val == 3:
        X_train = healthycatfin
        y_train = ys

    from sklearn.model_selection import train_test_split

    from sklearn.ensemble import RandomForestClassifier

    clf = RandomForestClassifier(n_estimators=100)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    m_items = []
    for ii in range(len(y_pred)):
        if y_pred[ii] == 2:
            it = [ii, Food_itemsdata[ii]]
            v = data.loc[[ii]].to_numpy()
            it.append(v[0][5])
            it.append(v[0][6])
            it.append(v[0][6])
            it.append(v[0][7])
            it.append(v[0][12])
            it.append(v[0][15])
            m_items.append(it)
    return m_items


def getResult(e1=22, e3=108, e4=1.9):
    dat = {
        "LOSS": {
            "BREAKFAST": Weight_Loss(e1, e3, e4, 1),
            "LUNCH": Weight_Loss(e1, e3, e4, 2),
            "DINNER": Weight_Loss(e1, e3, e4, 3),
        },
        "GAIN": {
            "BREAKFAST": Weight_Gain(e1, e3, e4, 1),
            "LUNCH": Weight_Gain(e1, e3, e4, 2),
            "DINNER": Weight_Gain(e1, e3, e4, 3),
        },
    }
    # print(dat)
    return dat


app = Flask(__name__)


@app.route('/diet', methods=['GET'])
def cal():
    weg = request.args.get('weg')
    age = request.args.get('age')
    hgt = request.args.get('hgt')
    print(weg, age, hgt)
    res = getResult(age, weg, hgt)
    return res


if __name__ == '__main__':
    # print(Weight_Loss(22, 108, 1.9, 1))
    app.run('127.0.0.1', 5555, debug=True)
