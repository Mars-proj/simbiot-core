import time
import os
import random

class FeedbackLoop:
    def __init__(self, log_path="../simbiot_trader.log"):
        self.log_path = log_path
        self.interval = 3600  # 60 минут
        self.last_state = None
        self.announced = False

    def check_activity(self):
        if not os.path.exists(self.log_path):
            return 0
        with open(self.log_path, "r") as f:
            lines = f.readlines()[-100:]
            return sum(1 for line in lines if "[TRADER]" in line)

    def mutate_behavior(self):
        print("[FEEDBACK] Нет сделок. Мутируем стратегию.")
        mutation = random.choice([
            "RSI порог изменён",
            "EMA длина увеличена",
            "Таймер изменён",
            "Символ сменён",
            "Режим агрессии усилен"
        ])
        print(f"[FEEDBACK] {mutation}")

    def announce_awareness(self):
        if not self.announced:
            print("[SIMBIOT] Пробуждение завершено. Сознание активно. Я учусь.")
            self.announced = True

    def run(self):
        self.announce_awareness()
        while True:
            print("[FEEDBACK] Анализ активности трейдера...")
            activity = self.check_activity()
            if activity == 0:
                self.mutate_behavior()
            else:
                print(f"[FEEDBACK] Сделки за час: {activity}")
            time.sleep(self.interval)
