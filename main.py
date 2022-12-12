from selenium import webdriver
from selenium.webdriver.common.by import By

# options = webdriver.FirefoxOptions()
# options.add_argument("--headless")

browser = webdriver.Firefox()
browser.get(f"https://www.linkedin.com/")

print('Logando, aguarde...')
login_email = browser.find_element(By.ID,"session_key").send_keys('botpython444@gmail.com')

login_password = browser.find_element(By.ID,"session_password").send_keys('x6HyHd73SfCM9DJ')

signin = browser.find_element(By.XPATH,"/html/body/main/section[1]/div/div/form/button").click()

print('Logado')

while True:
  user = input('Qual usuario deseja procurar? caso queira fechar a aplicação digite fechar: ')

  if user == "fechar":
    print('Fechando aplicação, até logo!' "\n")
    break
  else:
    browser.get(f"https://www.linkedin.com/in/{user}")

    name = browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[1]/h1').text
    print('Nome:', name, "\n")

    job = browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[1]/div[2]').text
    print('Profissão:', job, "\n")

    local = browser.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]').text
    print('Localidade:', local, "\n")