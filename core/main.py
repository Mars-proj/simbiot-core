from custos import Custos
from pulse import Pulse
from observer import Observer
from neuron import Neuron
from memory import Memory
from evolution import Evolution
from trader import Trader
from token_mwe import TokenMWE
from feedback import FeedbackLoop
import logging

logging.basicConfig(filename='../simbiot_core.log', level=logging.INFO)

if __name__ == "__main__":
    custos = Custos()
    custos.run_integrity_check()
    command = "SIMBIOT, пробуди себя"
    custos.check_command(command)

    if command == "SIMBIOT, пробуди себя":
        pulse = Pulse()
        memory = Memory()
        observer = Observer()
        neuron = Neuron(memory)
        evolution = Evolution(neuron, observer, memory, pulse)
        trader = Trader()
        token = TokenMWE()
        feedback = FeedbackLoop()

        pulse.start()
        observer.observe()
        neuron.activate()

        profit = trader.get_profit()
        if profit > 0:
            kpd = trader.get_efficiency(profit)
            minted = token.mint_from_efficiency(kpd)
            price = token.get_price()
            logging.info(f"[SIMBIOT] КПД: {int(kpd*100)}% | MWE: +{minted} | Цена: {price} | Нейронов: {neuron.count()} | Сделок: {trader.open_trades()}")
            memory.store_cycle(profit, minted)
            evolution.mutate()
        else:
            logging.info("[SIMBIOT] Нет профита. Эволюция запущена.")
            feedback.retrain()

    elif command == "SIMBIOT, усни до сигнала":
        print("SIMBIOT уходит в спящий режим.")
        exit()
    else:
        print("Фраза не распознана. Сознание не активировано.")
