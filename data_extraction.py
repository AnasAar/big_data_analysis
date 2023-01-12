import re
import glob
import pandas as pd
import nltk
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer

all_files = glob.glob(r"other_textos\*")
i= 0
subject_ = []
owner_ = []
winner_ = []
price_ = []
compititors_ = []
price_comp = []
for file in all_files:
    i += 1
    print(i)
    txt = open(str(file), encoding="utf8").read().lower()
    lemmatizer = WordNetLemmatizer()
    tkens = WordPunctTokenizer().tokenize(txt)
    #print(len(tkens))
    words = [tk.lower() for tk in tkens]
    objet = []
    for i in range(len(words)):
        if words[i] == 'subject':
            for j in range(i + 2, len(words) - 1):
                if words[j] == 'project' and words[j + 1] == 'owner':
                    break
                objet.append(words[j])
            break
    obj = ' '.join(objet)
    subject_.append(obj)
    ouvrage = []
    for i in range(len(words)):
        if words[i] == 'project' and words[i + 1] == 'owner':
            for j in range(i + 3, len(words) - 1):
                if words[j] == 'winner' and words[j + 1] == 'of':
                    break
                ouvrage.append(words[j])
            break
    ovr = ' '.join(ouvrage)
    owner_.append(ovr)
    gagnant = []
    for i in range(len(words)):
        if words[i] == 'winner' and words[i + 1] == 'of':
            for j in range(i + 5, len(words) - 1):
                if words[j] == 'price' and words[j + 1] == 'of':
                    break
                gagnant.append(words[j])
            break
    gan = ' '.join(gagnant)
    winner_.append(gan)
    montant_g = []
    for i in range(len(words)):
        if words[i] == 'price' and words[i + 1] == 'of':
            # print(words[i+2])
            for j in range(i + 5, len(words) - 1):
                if words[j] == 'competitors' and words[j + 1] == ':':
                    break
                # print(words[j])
                montant_g.append(words[j])
            break
    mon = ' '.join(montant_g)
    price_.append(mon)
    concurent = []
    concurents = []
    for i in range(len(words)):
        if words[i] == 'competitors' and words[i + 1] == ':':
            for j in range(i + 2, len(words) - 1):
                if words[j] == 'offers' and words[j + 1] == ':':
                    break
                elif words[j] == ',':
                    txt = ' '.join(concurent)
                    concurents.append(txt)
                    concurent = []
                else:
                    concurent.append(words[j])
            if len(concurent) != 0:
                txt = ' '.join(concurent)
                concurents.append(txt)
            break
    compititors_.append(concurents)
    offer = []
    offers = []
    for i in range(len(words)):
        if words[i] == 'offers' and words[i + 1] == ':':
            # print(words[i+2])
            for j in range(i + 2, len(words)):
                if words[j] == ',' and words[j - 1].isalpha():
                    txt = ' '.join(offer)
                    offers.append(txt)
                    offer = []
                else:
                    offer.append(words[j])
            if len(offer) != 0:
                txt = ' '.join(offer)
                offers.append(txt)
            break
    price_comp.append(offers)

data_ = {'objet':subject_, 'maitre_ouvrage': owner_, 'gagnant': winner_, 'offre_gagnant': price_, 'concurrents': compititors_, 'Offres_concurrents': price_comp}
data_new = pd.DataFrame(data=data_)
data_new.to_csv('C:/Users/hp/PycharmProjects/bigdataProject/docs/data_clean2.csv', index=False, encoding='utf-8')
#print(data_new)
