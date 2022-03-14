# -*- coding: utf-8 -*-

import numpy as np
from flask import Flask,request,render_template
from tensorflow import keras
from rdkit.Chem import rdMolDescriptors, MolFromSmiles, rdmolfiles, rdmolops
def ff(smile_string, radius=2, size=2048):
    mol = MolFromSmiles(smile_string)
    new_order = rdmolfiles.CanonicalRankAtoms(mol)
    mol = rdmolops.RenumberAtoms(mol, new_order)
    return rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius,
                                                          nBits=size,
                                                          useChirality=True,
                                                          useBondTypes=True,
                                                          useFeatures=False
                                                          )


app=Flask(__name__)


@app.route('/predict', methods=['GET'])
def predict():
	mod=keras.models.load_model('model1_nepochs_100')
	smiles_input=input("Enter your molecule SMILES for binary prediction: ")
	vec=np.frombuffer(ff(smiles_input).ToBitString().encode())
	vec=vec.reshape(1,-1)
	P_pred=mod.predict(vec)
	P=P_pred[0][0].astype(float)
	return "Binary prediction for: "+smiles_input+" is: "+str(int(P.round()))

if __name__=="__main__":
	app.run(debug=True)