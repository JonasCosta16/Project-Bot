# Project-Bot.
!!! ALERT !!!
Bot in constant evolution

A Bot That Creats Instagram Accounts. Made In Python Linguage. I did used Library PyAutoGUI and Time. Hope you like it!



import pyautogui
import time


#           --------------- Abrindo o Menu da Windowns e Digitando o Nome 'Chrome' ---------------
time.sleep(3)
pyautogui.press('winleft')
time.sleep(3)
pyautogui.write('chrome')
time.sleep(3)
pyautogui.press('enter')
time.sleep(3)
pyautogui.press('enter')
time.sleep(10)

#             --------------- Dentro do Google Digitar o Link do Site do Email Fake ---------------
pyautogui.write('https://moakt.com/pt/inbox')
pyautogui.press('enter')
time.sleep(7)

pyautogui.click(x=600, y=400) # Vai clicar no botão que tem lá que é pra gerar emails Aleatorios. Sla!!!
time.sleep(5)


pyautogui.click(x=750, y=285) # Ele vai gerar Outro Email Aleatorio
time.sleep(5)
pyautogui.click(x=680, y=285) # Clicar no Nome Copiar, Para copiar o Email Aleatorio






time.sleep(5) # Esperar 5 Segundos


#               --------------- Abrir Uma Janela Anônima ---------------
pyautogui.hotkey('ctrl', 'shift', 'n')
time.sleep(5)


#                  --------------- Dentro do Navegador Digitar o Link de Registrar do Instagram 
pyautogui.write('https://www.instagram.com/accounts/emailsignup/')
pyautogui.press('enter')

pyautogui.click(x=507, y=237) # coordenadas do campo de pesquisa no navegador
pyautogui.press('enter')

time.sleep(10) # Ele vai eseprar 10 segundos para que o Site do Instagram seja aberto completamente



pyautogui.click(x=600, y=350) # E-mail
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(x=600, y=400) # Nome Completo
pyautogui.write('Sofá de Cadeira')


pyautogui.click(x=600, y=450) # Nome de Usuário
time.sleep(3)
pyautogui.click(x=790, y=450)
time.sleep(3)


pyautogui.click(x=600, y=500) #Senha
pyautogui.write('maxstellesuametralhadora1')
time.sleep(3)


pyautogui.click(x=600, y=660) # Clicando No Botão 'Cadastre-se'


time.sleep(5)

pyautogui.click(x=600, y=320) # Data de Nacimento
pyautogui.click(x=600, y=380)
time.sleep(3)

pyautogui.click(x=700, y=320) # Mês de nascimento
pyautogui.click(x=700, y=380)
time.sleep(3)

pyautogui.click(x=750, y=320) # Ano de Nacimento
pyautogui.click(x=750, y=680)
time.sleep(3)

pyautogui.click(x=650, y=470) # Apertar no Botão Cadastre-se, um que aparece lá na parte quaando vamos colocar a data de nascimento
time.sleep(5)

pyautogui.click(x=1250, y=0) # Ele vai Minimizar a tela e ir diretamente para o Site E-mail Fake 
time.sleep(3)

pyautogui.doubleClick(x=400, y=350) # Ele vai atualizar o Email e esperar 7 segundos
time.sleep(7)

pyautogui.doubleClick(x=400, y=350) # Ele vai atualizar o Email e esperar 7 segundos DE NOVO!
time.sleep(5)

pyautogui.click(x=350, y=450) # Aqui ele vai clicar no primeiro nome que estiver na caixa de Entrada
time.sleep(10)

pyautogui.doubleClick(x=650, y=700) # Vai dar 2 cliques no Código que o instagram Mandar
pyautogui.hotkey('ctrl', 'c')
time.sleep(5)

pyautogui.hotkey('alt', 'tab') # Pra abrir aquelas barias Janelas, aí ele vai apertar na primeira que aparece, que é a Anônima do Instagram
time.sleep(3)
pyautogui.hotkey('enter')
time.sleep(3)

pyautogui.click(x=600, y=320) # Clica na Barrinha pra Inserir Código

pyautogui.hotkey('ctrl', 'v') # Cola o Código Do Instagram
time.sleep(3)

pyautogui.click(x=600, y=370) # Aperta no botão Continuar

