rq worker -s

# create venv
# install req of workflow module
# run worker script
# Create a new virtual environment
python3 -m venv myenv
source myenv/bin/activate
pip install -r ./mod/workflow1/requirements.txt
python3 