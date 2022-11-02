# build_files.sh
pip install -r requirements.txt
pip install python==3.9
cd venv
cd Scripts
activate
cd ..
cd .. 
python manage.py collectstatic