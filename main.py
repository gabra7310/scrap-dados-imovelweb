from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from openpyxl import load_workbook
from config import iniciachrome

links = open('links.txt', 'r')
sites = []
for link in links:
    sites.append(link.replace("\n", ""))

print(f"Dados para adicionar {len(sites)}")

pesquisa = load_workbook('pesquisa.xlsx')
planilha = pesquisa.active
numDados = 0
for cell in range(3,33):
    if planilha['D'+ str(cell)].value == None:
        pass
    else:
        numDados += 1

print(f"Dados presentes na planilha {numDados}")
linha = numDados + 3
amostra_adc = 1

for i in sites:
    driver = iniciachrome()
    driver.get(i)

    try:
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='article-container']/hgroup/h2[2]"))
        )
        endereco = driver.find_element_by_xpath("//*[@id='article-container']/hgroup/h2[2]").text
    except:
        endereco = ""



    try:
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='react-publisher-card']/div/div/span/h5"))
        )
        corretor = driver.find_element_by_xpath("//*[@id='react-publisher-card']/div/div/span/h5").text
    except:
        corretor = ""

    WebDriverWait(driver, 120).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='price-items']/span/span"))
    )
    valor_venda = driver.find_element_by_xpath("//div[@class='price-items']/span/span").text

    try:
        WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//i[@class='icon-scubierta']/ancestor::li"))
        )
        area_construida = driver.find_element_by_xpath("//i[@class='icon-scubierta']/ancestor::li").text
    except:
        area_construida = "0 Útil"
    try:
        dormitorios = driver.find_element_by_xpath("//i[@class='icon-dormitorio']/ancestor::li").text
    except:
       dormitorios = "0 Quarto"

    try:
        vagas = driver.find_element_by_xpath("//i[@class='icon-cochera']/ancestor::li").text
    except:
        vagas = "0 Vagas"

    try:
        banheiros = driver.find_element_by_xpath("//i[@class='icon-bano']/ancestor::li").text
    except:
        banheiros = "0 Banheiros"

    driver.execute_script("document.querySelector('#getPublisherData').click()")
    print("clickou")

    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='modal-mount']/div/div/div/ul/li[1]/a"))
        )
        tel = driver.find_element_by_xpath("//*[@id='modal-mount']/div/div/div/ul/li[1]/a").text
    except:
        tel = "0"
    print(tel)

    planilha['D' + str(linha)].value = endereco
    planilha['E' + str(linha)].value = corretor
    planilha['F' + str(linha)].value = tel
    planilha['G' + str(linha)].value = int(valor_venda.replace("R$ ", "").replace(".","").replace("%",""))
    planilha['I' + str(linha)].value = int(area_construida.replace(" ", "").replace("m²", "").replace("Útil", ""))
    planilha['J' + str(linha)].value = int(dormitorios.replace(" ", "").replace("Quartos", "").replace("Quarto", ""))
    planilha['K' + str(linha)].value = int(vagas.replace(" ", "").replace("Vagas", "").replace("Vaga", ""))
    planilha['L' + str(linha)].value = int(banheiros.replace(" ", "").replace("Banheiros", "").replace("Banheiro", ""))
    planilha['T' + str(linha)].value = i

    print(f"Amostra {amostra_adc}/{len(sites)} adicionada")
    amostra_adc += 1
    pesquisa.save('pesquisa.xlsx')
    linha += 1
    driver.quit()