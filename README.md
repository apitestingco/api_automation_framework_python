#### How to run the Project? 

- source venv/bin/activate
- pip install -r requirements.txt
- py.test  --alluredir=./reports test_scripts/githubrepo/test_*
> (If wants to see print message use)
> py.test  --alluredir=./reports test_scripts/githubrepo/test_* -s
- npm install allure
- allure serve reports

Source Code
![](https://i.imgur.com/RdNugjY.png)

Allure Report
![](https://i.imgur.com/bszcAdb.png)




How to Generate Token ?


Basic authentication using a password to the API is deprecated and will soon no longer work. Visit https://developer.github.com/changes/2020-02-14-deprecating-password-auth/ for more information around suggested workarounds and removal dates.
