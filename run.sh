(cd notebooks/public; python -m jupyter notebook --ip 0.0.0.0 --port ${PORT} --no-browser --allow-root --PasswordIdentityProvider.hashed_password ${JUPYTER_PWD_HASH})
