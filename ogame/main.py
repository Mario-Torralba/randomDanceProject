import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver_path = "C:/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--disable-extensions")

# Crear un objeto Service con la ruta del driver de Chrome
service = Service(driver_path)


path_to_profile = "C:/Users/torra/AppData/Local/Google/Chrome/User Data/Default"
options.add_argument("user-data-dir=" + path_to_profile)

# Pasar el objeto Service al constructor de Chrome
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

driver.get("https://lobby.ogame.gameforge.com/es_ES/hub")
time.sleep(4)

# # BOTON DE INICIAR SESION
# element = driver.find_element(By.CSS_SELECTOR, '.tabsList > li:nth-child(1)')
# element.click()
# time.sleep(2)
#
# # INPUT CORREO
# element = driver.find_element(By.CSS_SELECTOR, 'div.inputWrap:nth-child(2) > div:nth-child(2) > input:nth-child(1)')
# element.send_keys('torralba1995@gmail.com')
#
# # INPUT PASSWORD
# element = driver.find_element(By.CSS_SELECTOR, 'div.inputWrap:nth-child(3) > div:nth-child(2) > input:nth-child(1)')
# element.send_keys('antorcha1995')
#
# time.sleep(2)
#
# # CLICKAR EN INICIAR
# element = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(1)')
# element.click()
# element.click()
#
# time.sleep(6)
while True:
    # CLICKAR EN EL UNIVERSO UNDAE (ULTIMO JUGADO, ESTO QUIZAS HAYA QUE CAMBIARLO)
    element = driver.find_element(By.CSS_SELECTOR, 'button.button:nth-child(2)')
    element.click()

    time.sleep(4)

    #CERRAR LA NUEVA VENTANA Y QUEDARSE EN LA QUE SALE EL PLANETA PRINCIPAL
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[-0])
    driver.close()
    driver.switch_to.window(all_windows[-1])

    # SELECCIÓN DE BOTON DE PLANETA PRINCIPAL
    driver.get("https://s199-es.ogame.gameforge.com/game/index.php?page=ingame&component=fleetdispatch&cp=33622306")

    time.sleep(4)
    # SELECCIÓN DE BOTON DE FLOTA
    # element = driver.find_element(By.CSS_SELECTOR, '#menuTable > li:nth-child(9) > a:nth-child(2)')
    # element.click()

    # time.sleep(3)
    try:
        while True:

            element = driver.find_element(By.CSS_SELECTOR, '#js_eventDetailsClosed')
            element.click()

            time.sleep(1)

            element = driver.find_elements(By.CSS_SELECTOR, '#eventContent > tbody > tr')

            expedicionesTotales = 12
            expediciones451 = 0
            expediciones450= 0

            for e in element:
                td = e.find_elements(By.TAG_NAME, 'td')
                if(td[6].get_attribute('class') == 'icon_movement_reserve' and td[8].text == '[5:451:16]'):
                    expediciones451 = expediciones451 + 1
                if(td[6].get_attribute('class') == 'icon_movement_reserve' and td[8].text == '[5:450:16]'):
                    expediciones450 = expediciones450 + 1

            print(expediciones451, expediciones450)

            for i in range(6-expediciones451):

                element = driver.find_element(By.CSS_SELECTOR, '#allornone > div > div.firstcol.fleft > span > a')
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)

                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[2]/ul/li[2]/input')
                element.send_keys(700)
                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[2]/ul/li[5]/input')
                element.send_keys(1)
                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[1]/ul/li[10]/input')
                element.send_keys(1)
                time.sleep(1)

                # ENVIAR PRIMERO
                element = driver.find_element(By.CSS_SELECTOR, '#continueToFleet2 > span')
                element.click()

                time.sleep(2)

                # SISTEMA
                element = driver.find_element(By.CSS_SELECTOR, '#system')
                element.send_keys('451')

                # PLANETA
                element = driver.find_element(By.CSS_SELECTOR, '#position')
                element.send_keys('16')

                time.sleep(2)

                # SELECCIONAR EXPEDICION
                element = driver.find_element(By.CSS_SELECTOR, '#missionButton15')
                element.click()

                time.sleep(2)

                # ENVIAR
                element = driver.find_element(By.CSS_SELECTOR, '#sendFleet > span')
                element.click()

                time.sleep(3)

            for i in range(6-expediciones450):

                element = driver.find_element(By.CSS_SELECTOR, '#allornone > div > div.firstcol.fleft > span > a')
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)


                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[2]/ul/li[2]/input')
                element.send_keys(700)
                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[2]/ul/li[5]/input')
                element.send_keys(1)
                element = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div[2]/div[1]/div/div[7]/div/form/div/div[1]/ul/li[10]/input')
                element.send_keys(1)
                time.sleep(1)

                # ENVIAR PRIMERO
                element = driver.find_element(By.CSS_SELECTOR, '#continueToFleet2 > span')
                element.click()

                time.sleep(2)

                # SISTEMA
                element = driver.find_element(By.CSS_SELECTOR, '#system')
                element.send_keys('450')

                # PLANETA
                element = driver.find_element(By.CSS_SELECTOR, '#position')
                element.send_keys('16')

                time.sleep(2)

                # SELECCIONAR EXPEDICION
                element = driver.find_element(By.CSS_SELECTOR, '#missionButton15')
                element.click()

                time.sleep(2)

                # ENVIAR
                element = driver.find_element(By.CSS_SELECTOR, '#sendFleet > span')
                element.click()

                time.sleep(3)

            # TIEMPO ENTRE BUSQUEDA DE EXPEDICIONES
            time.sleep(300)

            driver.get("https://s199-es.ogame.gameforge.com/game/index.php?page=ingame&component=fleetdispatch&cp=33622306")

            time.sleep(4)

    except:

        print("Se ha deslogeado, logeando de nuevo")
