### A service for shortening URLs and further redirection to the shortened link.
#### Libraries: Python 3.12, FastAPI, uvicorn, httpx, flake8
Launch instructions:
1. activate virtual environment -> poetry shell
2. install requirements -> poetry install
3. run app with command -> uvicorn main:app --reload
4. Try POST-request long url:
- Post request long URL
![img_1.png](img/POST_url.png)

- Response short_url for redirect to original address (Location)
![img_2.png](img/GET_url.png)
