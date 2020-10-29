# ElasticsearchPoc
# Objective

"By This Poc We can create only indices and insert record for indices":

You will need the following programmes properly installed on your computer.<br>
Python 3.7+<br>
django 2.2+<br>
Virtual Environment To install virtual environment on your system use:<br>
pip install virtualenv<br>

or

pip3 install virtualenv #if using linux(for python 3 and above)<br>

# Installation and Running :

git clone https://github.com/ongraphpythondev/ElasticsearchPoc.git
cd Elasticsearch
virtualenv venv or virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows or source venv/bin/activate # for linux

Install required packages for the project to run

pip install -r requirements.txt
python manage.py runserver
# Elastic Search Setup

1.Install ElasticSearch<br>
  (For Windows Install Elasticsearch windows Installer)
# Start Server for Local
1.python manage.py runserver

# For Operation (Open Browser and follow the step)

1.indices/create/Name of Indices/   (For create indices)<br>
# Get Indices List
  http://localhost:9200/_cat/indices
2.inges/create/indices Name      (For Insert Payload for indices)<br>
# Get List of Inserted Payload for with indices
  http://localhost:9200/Name of Indices
 

