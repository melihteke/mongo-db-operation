## MongoDB Python CRUD Operations

This project provides a simple Python interface for performing CRUD (Create, Read, Update, Delete) operations on a MongoDB database using the PyMongo library.
Before using this code, you need to have a prebuilt MongoDB installed on your system or somewhere else.

### Installation

```sh
git clone https://github.com/melihteke/mongo-db-operation.git
```

```sh
pip install -r requirements.txt
```

#### Create .env file in to relative root directory and fill in below variables
```sh
DB_URI=mongodb+srv://<DB_USERNAME>:<DB_PASSWORD>@cluster0.ybl2347fog.mongodb.net/test?retryWrites=true&w=majority
DB_NAME=<DB_NAME>
DB_COLLECTION_NAME=<DB_COLLECTION_NAME>
```



#### Usage
```sh
from mongodb_operation import MongoDBOperation
operation = MongoDBOperation()
```

```sh
In [10]: operation.view_all_records()
Out[10]: 
[{'_id': ObjectId('6437044444336b29c882e327'),
  'name': 'June',
  'surname': 'Williams'},
 {'_id': ObjectId('6437088f63c471c0c778a80a'),
  'name': 'July',
  'surname': 'Killiams'}]
  ```
  
