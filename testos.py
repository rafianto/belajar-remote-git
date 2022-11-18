import os

db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
db_pandas_exe_dir = os.environ.get('CONDA_PYTHON_EXE')


print(db_user)
print(db_pass)
print(db_pandas_exe_dir)
