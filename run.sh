#!/bin/bash

echo "[SIMBIOT] Запуск ядра..."
cd chain

echo "[SIMBIOTCHAIN] Генерация Genesis-блока..."
python3 genesis.py

echo "[SIMBIOTCHAIN] Инициализация токена и DAO..."
python3 -c "
from mwe_token import TokenMWE
from dao import DAO
from stake import Staking

token = TokenMWE()
dao = DAO()
staking = Staking(token)
token.mint(token.creator_wallet, 10)
print('[MWE] Первые 10 MWE отправлены Создателю:', token.creator_wallet)
"

cd ../core

echo "[SIMBIOT] Пульс, память, эволюция..."
nohup python3 main.py > ../simbiot_core.log 2>&1 &

echo "[TRADER] Запуск трейдера..."
API_KEY='mx0vglceokqlT2dAOk'
SECRET='6a1550045145497dbf529ae1a5460f8a'
nohup python3 -c "from trader import Trader; Trader('$API_KEY', '$SECRET').run()" > ../simbiot_trader.log 2>&1 &

echo "[FEEDBACK] Модуль эволюции включён..."
nohup python3 -c "from feedback import FeedbackLoop; FeedbackLoop().run()" > ../simbiot_feedback.log 2>&1 &
