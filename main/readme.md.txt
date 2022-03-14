SERVIER -- Data Science technical test --  March 2022

______________________________________________________
What the module main.py can do and how to use it:

main.py is a python module containing functions specifically designed to train, evaluate and do predictions through deep learning from datasets in csv format that includes binary properties of single stranded molecules. The key data transformation is to translate each smiles representation to a 256 dimensions vector using some of the Morgan Fingerprints obtained from rdkit-pypi python module.

______________________________________________________________
***** ENVIRONMENT SETTINGS TO USE THE MODULE : main.py *****

Works on Linux, MacOS opearting systems or Windows through Anaconda Prompt (anaconda3), Python 3.6.13:

1. cd to your path directory containing the following files:
______________________________________

-main.py
-feature_extractor.py
-requirements.txt
-your datasets


2.Copy paste the following commands:
______________________________________

wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda 
export PATH=~/miniconda/bin:$PATH
conda update -n base conda
conda create -y --name servier python=3.6
conda activate servier
conda install -c conda-forge rdkit
pip install -r requirements.txt


You should be all set.
______________________________________
______________________________________
______________________________________
______________________________________


**************     USING THE MODULE       **********************

Make sure your (servier) environment is activated. Open python.
To import all the functions of the module and start training a model:



>>>from main import *
>>>go()



Then follow instructions on the prompt.

_____________________________________TECHNICAL DESCRIPTION OF THE MODULE FUNCTIONS

This module includes 8 functions:

1. read_dataset(dataset) 
This function takes a dataset path as only argument. The dataset must be a coma separated data file. Calling the function will import the dataset and turn it into a list of dictionnaries corresponding to each rows of the dataset, the dictionnaries keys being the columns name. Returns "df" the dictionnaries list object. This format has been proved to be effective to improve time calculation for iterating process other numerous data rows.


2. data_process(list_dictionnaries)
This function takes a list of dictionnaries as returns with the precedent function (1.) as only argument. 
It initialize two empty matrices, Y and X_vec, it iterates over every rows of the list of dictionnaries and append the binary property in the Y matrix and process the corresponding molecule smiles representations to a 256 dimensions vector in the X_vec matrix. Returns Y and X_vec matrices.

3. modeldl()
This function compile a simple sequential dense neural network (fully-connected) which is the simplest deep learning model with three layers. The input layers has 256 neurons which correspond to the dimension of the vectorized molecule fingerprints, the hidden layer has 128 neurons and the output layer has 1 neuron. This single neuron output has a sigmoid activation function and a binary crossentropy loss function as standard fare for binary classification. The function compiles the model, display summary and return the model as "model". This function does not take any argument as developed so far.

4. data_split(X,y)
This function takes two arguments. X and y matrices and split it to train (0.9) and test (0.1) data set. The function returns X_train, X_test, y_train, y_test.


5. train(model,X_train,y_train)
This function takes three arguments: - model - a pre-compiled deep learning model as returned by function (3.), and X_train and y_train the matrices training dataset we want to train the model with. To use this function with your own pre-compiled model make sure to primaraly set these three variables: "epoch" to an integer corresponding to the number of epochs,"name" to a string that will be used to save your model and "path" which should correspond to your current directory. Return the training history that can further be used to evaluate and visualize real-time loss VS epoch graph. 

6. evaluate(model,X_test,y_test)
This function takes three arguments: - model - a pre-trained model you want to evaluate using test datasets X_test and y_test.
Return score, that contains the evaluation results of the evaluation.

7. predict(model)
This function takes a model as a single argument. If called it will ask you by the prompt to enter a smiles that will be converted in a 256 dimensions vector using some fingerprints (the same process applied in function (2.)). The model will predict the binary property of this molecule as a number between 0 and 1. The function returns this prediction as P_pred.

8. go()
This function should be called to properly read,process and split your dataset, compile, train and evaluate your deep learning model. It is using all the 7 functions above and will ask on the prompt the name you want to create for your model (name), the number of epochs you want your model to be trained on (epoch), the name of the data set you wish to use (ie. dataset_single, dataset_multi)(csv), the name of the binary property column in your dataset (ie. P1, P2 .... P6)(P_col), the name of the smiles columns in your dataset (in this case "smiles")(smiles_col). It is using the os module to get your current directory (path) to help localize your dataset (data). It returns the following objects: name,epoch,csv,P_col,smiles_col,path,data,df,Y,X_vec,model,X_train,X_test,y_train,y_test