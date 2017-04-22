import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close()

sue['pay'] *= 2.5
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close()
