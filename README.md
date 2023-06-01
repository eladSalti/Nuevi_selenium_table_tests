In order to run the tests you need to activate the python env and open from the root folder of the project
run the following command - $ pytest --html=report.html. This command will run all the tests and will create a new
pytest html report.
If you want to run a single test run the following command - $ pytest -m <The test name>, you can find the tests name
in the test body @pytest.mark.<test name>.



