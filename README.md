# Test Testnet Binance API and calculate 95 percentile
Selenium/Python

```
The Task 1
1. Send a request to https://testnet.binance.vision for ETHBTC
2. Check results

The Task 2
1. Send 20 requests to https://testnet.binance.vision for ETHBTC according to Rate limits
2. Check results
```

Use python 3.8 +
Create and activate virtual environments

```
python3 -m venv env
source env/bin/activate
```

Run in terminal

```
pip install -r requirements.txt
```

Start the test from a folder which contains test file(you also can --headless option)
```
Ex: cd ../Binance_test
pytest test_percentile.py

Or using in headless mode:
pytest test_percentile.py --headless true
```

If you want to get Allure report
```
pytest test_percentile.py --alluredir=allure-results/
allure serve allure-results/
```

pre-commit https://pre-commit.com
```
pre-commit run --all-files
```

Test site
```
https://testnet.binance.vision
```
