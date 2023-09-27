This repository was created for the course "Automation Testing with Python and Selenium". 

This code launches a test that checks the button "Add to the basket" on page http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.

Before starting you should install virtual environments. To do it type in your cmd:
<code>
python -m venv venv{your env name}
venv\Scripts\activate
pip install -r requirements.txt
</code>

To start the test with Firefox and French language type in cmd: <br><code>pytest --language=fr --browser_name=firefox test_items.py</code>
