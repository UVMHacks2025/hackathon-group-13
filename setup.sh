rm -r env
echo Creating Virtual Environment
python -m venv env
. env/Scripts/activate
echo Installing Requirements
pip install -r requirements.txt
echo Finished