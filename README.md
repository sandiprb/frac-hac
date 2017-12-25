# Hackathon Challenge

## Basic Structure
The structure is as follows:
* data: has the datasets files. Create it if it doesn't exist and put compressed gz data files there.
* modules: has the custom modules created by us
* notebooks: has the jupyter notebooks

## Repo Structure
The repo has following branch structure which is to be followed while working and commiting the code:
* **master**: Main branch only for working releases
* **pre-master**: When working on code this is the branch you pick up the code from.
* **feature**: Best explained through example. So if you want to work on creating modules, simply create a "create-modules" branch from the latest HEAD revision of "pre-master" branch. Code like mad on the _create-modules_ branch and when you feel ready merge your changes into the _pre-master_