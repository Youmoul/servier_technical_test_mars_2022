# servier_technical_test_mars_2022
Data Science technical test

/Youmoul/servier_technical_test_mars_2022
_____________________________________________

/main/

Containing main.py module and a detailed readme.md.txt file on how to use and process the datasets as well as train and evaluate deep learning models for binary prediction of SMILES molecules representation.
_____________________________________________

/models/

model1 for P1 prediction and a model3 for P9 prediction, both trained on 100 epochs using the module main.py as explained in the readme.md.txt in the main repository. model2 has not been developed due to the technical incoherances with its definition. 
_____________________________________________

/servier_flask_api/

A simple flask api turn into an application to predict the binary property for any given SMILES molecule (using model1) that can be install in a conda virtual environment with the following commands in your shell environment.

If you already have an environment with git, python and pip the following commands should install and display the application:


git clone https://github.com/Youmoul/servier_technical_test_mars_2022/servier_flask_api test <br />
cd test/servier_flask_api <br />
pip install -r requirements.txt <br />
python setup.py install <br />
servier <br />



Else copy paste the following commands:

wget --quiet https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh <br />
Miniconda3-latest-Linux-x86_64.sh -b -p ~/miniconda <br />
export PATH=~/miniconda/bin:$PATH <br />
conda update -n base conda <br />
conda create -y --name servier python=3.6 <br />
conda activate servier <br />
conda install -c conda-forge rdkit <br />
conda install -c conda-forge git <br />
git clone https://github.com/Youmoul/servier_technical_test_mars_2022/servier_flask_api test <br />
cd test/servier_flask_api <br />
pip install -r requirements.txt <br />
python setup.py install <br />
servier <br />


__________________________________________

Personal information to the recruitor: 
Very sadly I had to develop these codes on my old personal laptop with Anaconda3 prompt / Notepad++ on Windows and additionally ran out of memory storage while installing Docker at the last moment... Hence I can not demonstrate my Docker command and provide my optimized application image in due time. Sorry for the inconveniancy.

:)

