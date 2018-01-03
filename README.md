# Hackathon Challenge

## Basic Structure
The structure is as follows:
* data: has the datasets files. Create it if it doesn't exist and put compressed gz data files there.
* modules: has the custom modules created by us
* notebooks: has the jupyter notebooks
* app: has the entire webapp code

## Git workflow
The repo has following branch structure which is to be followed while working and commiting the code:
* **master**: Main branch only for working releases
* **pre-master**: When working on code this is the branch you pick up the code from.
* **feature**: Best explained through example. So if you want to work on creating modules, simply create a "create-modules" branch from the latest HEAD revision of "pre-master" branch. Code like mad on the _create-modules_ branch and when you feel ready merge your changes into the _pre-master_


## WebApp

**Setup**

```
clone the repo

create & activate virtualenv

pip install -r requirements.txt

python -m spacy download en


# install node js & yarn
curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install nodejs
sudo apt-get install build-essential


# Verify installation
node --version

sudo npm install yarn -g
```


Setting up node js front-end dependecincies
```
make deps
```


Bootup app
```
make run
```

_refer to Makefile for details on make commands_



## Other important links
 - [Using PyMongo with flask](http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php)
 - [Full-Text Search in MongoDB](https://code.tutsplus.com/tutorials/full-text-search-in-mongodb--cms-24835)
 - [Flask Series: Views and Web Forms](https://damyanon.net/post/flask-series-views/)
 - [Spacy english module](https://spacy.io/usage/models)
