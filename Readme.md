create env

'''bash
pip install pipenv

'''bash
pipenv install

activate environment
'''bash
pipenv shell

Create Requirement File
install the requirements
'''bash
pip install -r requirements.txt

download the data from
https://data.world/marineinstitute/af72802a-fb7a-46ef-9b98-d21421954fdd/workspace/file?filename=download-csv-6.csv

'''bash
git init
'''bash
dvc init
'''bash 
dvc add data_given/winequality.csv
'''bash
git add .
'''bash
git commit -m "first commit"

oneliner updates for readme
'''bash
git add . && git commit -m "update Readme.md"
'''bash
git remote add origin https://github.com/Hamshita/ferry_route.git
'''bash
git branch -M main
git push origin main
tox command -

tox
for rebuilding -

tox -r 
pytest command

pytest -v
setup commands -

pip install -e . 
build your own package commands-

python setup.py sdist bdist_wheel

