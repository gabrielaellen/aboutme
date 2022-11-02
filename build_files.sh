# build_files.sh
pip install -r requirements.txt
cd venv
cd Scripts
activate
cd ..
cd .. 
python3.9 manage.py collectstatic