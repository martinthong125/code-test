# script1.py
import pickle

x = 5
with open("variable.pkl", "wb") as f:
    pickle.dump(x, f)
