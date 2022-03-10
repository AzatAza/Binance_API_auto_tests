import pytest
import requests
import time
import math
import numpy as np
from ratelimit import limits, sleep_and_retry
base_url = 'https://testnet.binance.vision?symbol=ETHBTC'
route = '/api/v3/depth'
pair = 'ETHBTC'
PERCENTILE = 95
ITERS = 20
ONE_SECOND = 1
ONE_MINUTE = 60
DAY = 86400


class TestBinance:
    def test_order_book(self):
        """
        1. Send a request to Binance testnet
        2. Assert the server's response
        """
        r = requests.get(f'{base_url}{route}?symbol={pair}')
        assert r.status_code == 200

    @sleep_and_retry
    @limits(calls=10, period=ONE_SECOND)
    @limits(calls=1200, period=ONE_MINUTE)
    @limits(calls=100000, period=DAY)
    @pytest.mark.parametrize('limit', [100, 500, 1000, 5000])
    def test_percentile(self, limit):
        """
        1. Send 20 requests for each limit
        2. Get time response and calculate 95 percentile for each limit
        """
        global res
        total = []
        for i in range(ITERS):
            start = time.time()
            res = requests.get(f'{base_url}{route}?symbol={pair}&limit={limit}')
            end = time.time()
            total.append(end - start)
        need_to_delete = math.ceil(ITERS * ((100 - PERCENTILE) / 100))
        for k in range(need_to_delete):
            total.remove(max(total))
        if res.status_code != 200:
            raise Exception('API response: {}'.format(res.status_code))
        print('\n95 перцентиль времени ответа сервера при limit = {}: {} секунд.'.format(limit, np.mean(total)))


TestBinance()
