# RHDZMOTA Notebooks

## Setup & Installation

[Recommendation] Create a python virtual environment with python. You can use [this blogpost](https://rhdzmota.com/post/the-best-way-to-install-python/) as a reference.
* `$ pyenv exec python -m venv venv`
* `$ source venv/bin/activate` or `source venv/Scripts/activate`

Install the python dependencies:

```commandline
$ pip install -r requirements.txt
```

The current repo provides a `.env.example` with a set of default variables. We highly recommend updating these values to increase your project security:
* Create your own `.env` via: `cp .env.example .env`
* Update the `PORT`.
* Update the Jupyter Password Hash `JUPYTER_PWD_HASH`.

You can create your own password hash via the following script execution:

```commandline
$ python jupyter_password_hash.py create --pwd <your-password>
```
* The password can also be provided via en env.var or by user-input.


## Run The Service

Be sure that the environment variables are correctly set (e.g., `export $(cat .env | xargs)`). Then execute:

```commandline
$ bash run.sh
```
