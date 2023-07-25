# selenium 4.1用
# MUTABIND2のスクレイピング用

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

# TODO
# PROCESS
process = "process"
# process = "min_process"
# WILD TYPE
protein = "5uv8"
mutation = "K397W"
# MUTANT
# protein = "5uwc"
# mutation = "W397K"
# common
mutation_chain = "B"
email_address = "20a1004c@shinshu-u.ac.jp"

service = Service(executable_path="./../chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

trj_num = "trj01"
run_num = 13
data_path = f"/home/komadori/documents/ppi_scr_v2/data/{process}/{protein}/{trj_num}_run{run_num}_edit_atom.pdb"

driver.get('https://lilab.jysw.suda.edu.cn/research/mutabind2/')

# pdbファイルのアップロード
upload_input = driver.find_element(By.ID, "pdb_file_input")
upload_input.send_keys(data_path)

# mutationの種類の決定ボタンを押す
submit_btn = driver.find_element(
    By.XPATH, '//*[@id="single"]')
submit_btn.click()

# 数秒待つ

# ドラッグ＆ドロップ
source_A = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[1]/div/div/ul/li[1]/h5')
source_B = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[1]/div/div/ul/li[2]/h5')
target_A = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div[3]/form/div/div/div[1]')
target_B = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div[3]/form/div/div/div[2]')

actions = ActionChains(driver)
actions.drag_and_drop(source_A, target_A)
actions.perform()

actions.drag_and_drop(source_B, target_B)
actions.perform()
sleep(3)
# nextボタンを押す
next_btn = driver.find_element(
    By.XPATH, '/html/body/div[2]/div[2]/div[4]/div[2]/button')
next_btn.click()

sleep(30)
