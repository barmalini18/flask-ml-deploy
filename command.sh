sh Miniconda3-py37_4.10.3-Linux-x86_64.sh
export PATH=~/miniconda3/bin:$PATH
git clone git@github.com:barmalini18/flask-ml-service.git
cd flask-ml-service
conda create -n env -f requirements.txt
conda activate
make all
az webapp up --name tb-housepriceapi --resource-group ODL-clouddevops-212363 --runtime "PYTHON:3.7"
