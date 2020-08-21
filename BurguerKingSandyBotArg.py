#Autor:jmlgonez73

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

#info= input('Datos: (17441 14 08 08 28 pm)\n')
#info= info.split()
if len(sys.argv) == 7:
    print("pass")
else:
    print("FALLO")
    sys.exit()

driverPath = "C:/WINDOWS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath)
driver.get('https://www.miexperienciabkespana.com/')


#Introduccion de todos los datos
def fase_1():
    driver.find_element_by_xpath('//*[@id="NextButton"]').click()
    driver.find_element_by_id("SurveyCode").send_keys(sys.argv[1])
    driver.find_element_by_id("InputDay").send_keys(sys.argv[2])
    driver.find_element_by_id("InputMonth").send_keys(sys.argv[3])
    driver.find_element_by_id("InputHour").send_keys(sys.argv[4])
    driver.find_element_by_id("InputMinute").send_keys(sys.argv[5])
    driver.find_element_by_id("InputMeridian").send_keys(sys.argv[6])
    driver.find_element_by_xpath('//*[@id="NextButton"]').click()

#Bucle y progreso de la encuesta
def fase_2():
    present=True
    porcentaje="0%"
    while present:
        #Si hay elementos con ese nombre de clase
        if len(driver.find_elements_by_class_name("ValCode"))> 0 :
            present=False
        else:
            driver.find_element_by_xpath('//*[@id="NextButton"]').click()   
        #si hay elementos con esa id
        if len(driver.find_elements_by_id("ProgressPercentage"))>0:
            if driver.find_element_by_id("ProgressPercentage").text != porcentaje:#No repito valores
                porcentaje= driver.find_element_by_id("ProgressPercentage").text
                print(porcentaje)
            
    print(driver.find_element_by_class_name("ValCode").text)
   
def main():
    fase_1()
    fase_2()
    driver.close()

main()