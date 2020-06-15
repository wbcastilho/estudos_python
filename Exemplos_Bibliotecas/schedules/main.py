# Schedules - 
# Caso não tenha instalado, instale o schedule da seguinte maneira:
# pip install schedule

import schedule
import time

def Tarefa():
    print('Gerando grana...')

# Executar a cada 10 segundos
schedule.every(10).seconds.do(Tarefa)

# Executar pelo dia da semana
#schedule.every().monday.do(Tarefa)

# Executar pelo dia da semana em um horário espeecífico
#schedule.every().monday.at('08:00')do(Tarefa)

# Executar todo dia em um horário espeecífico
#schedule.every().day.at('08:00')do(Tarefa)

while 1:
    schedule.run_pending()
    time.sleep(1)