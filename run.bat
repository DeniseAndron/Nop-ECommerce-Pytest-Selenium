rem pytest -s -v -m "sanity" --html=./Reports/sanity.html testCases --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/sanity.html testCases --browser chrome
pytest -s -v -m "sanity and regression" --html=./Reports/sanity.html testCases --browser chrome

