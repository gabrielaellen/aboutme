# build_files.sh
pip install -r requirements.txt
./venv/Scripts/activate 
python3.8 manage.py collectstatic