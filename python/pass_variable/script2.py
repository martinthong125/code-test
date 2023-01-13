# script2.py
import pickle

with open("variable.pkl", "rb") as f:
    x = pickle.load(f)
print(x)
