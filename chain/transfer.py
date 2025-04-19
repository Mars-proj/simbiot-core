from token import TokenMWE

class Transfer:
    def __init__(self, token: TokenMWE):
        self.token = token

    def execute(self, sender, recipient, amount):
        result = self.token.transfer(sender, recipient, amount)
        if result:
            print(f"Успешно: {amount} MWE переведено от {sender} к {recipient}")
        else:
            print("Ошибка: недостаточно средств или превышена комиссия.")
        return result
