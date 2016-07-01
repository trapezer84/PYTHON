import pickle

colors = ['blue', 'red', 'white']

f = open('test.txt', 'w')
pickle.dump(colors, f)
f.close()