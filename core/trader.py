import ccxt
import time
import logging

class Trader:
    def __init__(self, api_key, secret, exchange_name="mexc", neuron_name="Unnamed"):
        self.api_key = str(api_key)
        self.secret = str(secret)
        self.exchange_name = exchange_name.lower()
        self.neuron_name = neuron_name
        self.exchange = self.connect_exchange()

    def connect_exchange(self):
        try:
            exchange_class = getattr(ccxt, self.exchange_name)
            exchange = exchange_class({
                'apiKey': self.api_key,
                'secret': self.secret,
                'enableRateLimit': True,
                'options': {'adjustForTimeDifference': True}
            })
            exchange.check_required_credentials()
            exchange.load_markets()
            return exchange
        except Exception as e:
            print(f"[ERROR] Биржа {self.exchange_name} не распознана или ошибка подключения: {e}")
            return None

    def get_balance(self):
        try:
            balance = self.exchange.fetch_balance()
            return balance['total'].get('USDT', 0)
        except Exception as e:
            logging.error(f"[{self.neuron_name}] Ошибка при получении баланса: {e}")
            return 0

    def get_market_symbol(self):
        try:
            markets = self.exchange.load_markets()
            for symbol in markets:
                if symbol.endswith("/USDT") and markets[symbol]['active']:
                    return symbol
        except Exception as e:
            logging.error(f"[{self.neuron_name}] Ошибка при получении пары: {e}")
        return None

    def run(self, log_path="/dev/null"):
        logging.basicConfig(filename=log_path, level=logging.INFO)
        if not self.exchange:
            logging.error(f"[{self.neuron_name}] Биржа не подключена.")
            return

        while True:
            try:
                balance = self.get_balance()
                if balance < 10:
                    logging.info(f"[{self.neuron_name}] Баланс ниже минимального порога (10 USDT): {balance}")
                    time.sleep(60)
                    continue

                symbol = self.get_market_symbol()
                if not symbol:
                    logging.info(f"[{self.neuron_name}] Торговая пара не найдена.")
                    time.sleep(60)
                    continue

                ticker = self.exchange.fetch_ticker(symbol)
                price = ticker['last']
                max_trade_amount = round((balance * 0.1) / price, 6)  # 10% от баланса
                if max_trade_amount * price < 10:
                    logging.info(f"[{self.neuron_name}] Сумма сделки < 10 USDT. Пропускаем.")
                    time.sleep(60)
                    continue

                order = self.exchange.create_market_buy_order(symbol, max_trade_amount)
                logging.info(f"[{self.neuron_name}] BUY {max_trade_amount} {symbol} по {price} | ордер ID: {order['id']}")

            except Exception as e:
                logging.error(f"[{self.neuron_name}] Ошибка в торговле: {e}")

            time.sleep(300)
