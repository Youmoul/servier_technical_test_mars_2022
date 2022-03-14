# servier_technical_test_mars_2022
Data Science technical test

Repositories:

main: 

Containing main.py module and a detailed readme.md file on how to use and process the datasets as well as train and evaluate deep learning models for binary prediction of SMILES molecules

models:

Saved keras models:
model1 for P1 prediction and an example of model3 for P9 prediction, both trained on 100 epochs using the module main.py as explained in the readme.md in the main repository.

servier_flask_api:

A simple flask api to get the binary prediction for any given SMILES molecule (using model1) that can be install in a conda virtual env with the following commands in your shell environment:

wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda 
export PATH=~/miniconda/bin:$PATH
conda update -n base conda
conda create -y --name servier python=3.6
conda activate servier
conda install -c conda-forge rdkit
pip install -r requirements.txt
python setup.py install
git clone https://github.com/Youmoul/servier_technical_test_mars_2022/servier_flask_api test
cd test/servier_flask_api
python setup.py install
servier
