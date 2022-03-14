# -*- coding: utf-8 -*-

#Servier technical test, 14th March 2022, Mxxxxx Cxxxxx, mxxxxx.cxxxxx@gmail.com

import os
import numpy as np
import pandas as pd
import tensorflow as tf
import keras
from feature_extractor import fingerprint_features as ff
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense

#####################FUNCTIONS##########################


def read_dataset(dataset):
	df=pd.read_csv(dataset,sep=",")
	df=df.to_dict('records')
	return df
	
def data_process(list_dictionnaries):
	Y=[]
	X_vec=[]
	for row in list_dictionnaries:
		Y.append(row[P_col])
		X_vec.append(np.frombuffer(ff(row[smiles_col]).ToBitString().encode()))
	Y=np.asarray(Y)
	X_vec=np.asarray(X_vec)
	
	return Y,X_vec

def modeldl():
	model=Sequential()
	model.add(Dense(128, input_shape=(256,)))
	model.add(Dense(1,activation='sigmoid'))
	model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])
	model.summary()
	return model
	
def data_split(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
	print("Data has been split to train and test sets")
	return X_train, X_test, y_train, y_test
	
def train(model,X_train,y_train):
	history=model.fit(X_train, y_train, epochs=int(epoch), batch_size=32)
	model.save(name+"_nepochs_"+epoch)
	print("Model saved as: "+name+"_nepochs_"+epoch+" in: "+path)
	return history
	
def evaluate(model,X_test,y_test):
	score = model.evaluate(X_test, y_test, verbose = 0) 
	print("_________Model evaluation on test set__________")
	print('Loss:   '+str(score[0])) 
	print('Metric:   '+str(score[1]))
	return score

def predict(model):
	mod=keras.models.load_model(model)
	smiles_input=input("Type or copy a smiles representation for any molecule:")
	vec=np.frombuffer(ff(smiles_input).ToBitString().encode())
	vec=vec.reshape(1,-1)
	P_pred=mod.predict(vec)
	P=P_pred[0][0].astype(float)
	print("Binary prediction for: "+smiles_input+" is: "+str(int(P.round())))
	return P

def go():
	global name
	name=input("Please enter name for your model to be saved:")
	global epoch
	epoch=input("Enter the number of epoch you want to train your model with:")
	global csv
	csv=input("Enter the name of your dataset (must be in the directory you are working on):")
	global P_col
	P_col=input("Enter the name of your column containing Binary property to be predicted:")
	global smiles_col
	smiles_col=input("Enter the name of your column containing the smiles of your molecules:")
	global path
	path=os.getcwd()
	global data
	data=path+"/"+csv+".csv"
	global df
	df=read_dataset(data)
	global Y,X_vec
	Y,X_vec=data_process(df)
	global model
	model=modeldl()
	global X_train, X_test, y_train, y_test 
	X_train, X_test, y_train, y_test=data_split(X_vec, Y)
	train(model,X_train,y_train)
	evaluate(model,X_test,y_test)