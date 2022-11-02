# build_files.sh
pip install -r requirements.txt
./venv/Scripts/Activate
python3.9 manage.py collectstatic