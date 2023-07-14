# selenium 4.10用
# selenium 4.10から、web_drive_managerが上手く機能しない

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By  # locate elements
from selenium.webdriver.chrome.service import Service

# TODO
# protein = "5uv8"
# mutation = "K397W"
protein = "5uwc"
mutation = "W397K"
mutation_chain = "B"
email_address = "20a1004c@shinshu-u.ac.jp"
process = "process"
# process = "min_process"

for i in range(10):
    trj = i + 1

    if (trj < 10):
        trj_num = f"trj0{trj}"
    else:
        trj_num = f"trj{trj}"

    # url保存ファイルの作成
    url_path = f"/home/komadori/documents/ppi_scr_v2/result/url/{protein}/{process}/mcsm_url_{protein}_{trj_num}.txt"
    fw = open(url_path, 'w')
    fw.write('')
    fw.close()

    service = Service(executable_path="./../chromedriver")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    for j in range(10):
        run_num = j + 13

        data_path = f"/home/komadori/documents/ppi_scr_v2/data/{process}/{protein}/{trj_num}_run{run_num}_edit_atom.pdb"
        # data_path = f"/home/komadori/documents/ppi_scr_v2/data/{process}/{protein}/{protein}_{trj_num}_run{run_num}_min_edit.pdb"

        driver.get('https://biosig.lab.uq.edu.au/mcsm_ppi2/submit_prediction')

        print(f"run{run_num}")

        # pdbファイルのアップロード
        upload_input = driver.find_element(By.ID, "pdb_file_single")
        upload_input.send_keys(data_path)

        # 変異残基の指定
        mutation_text = driver.find_element(By.ID, "mutation_single")
        mutation_text.send_keys(mutation)

        # 鎖名の指定
        chain_text = driver.find_element(By.ID, "chain_single")
        chain_text.send_keys(mutation_chain)

        # メールアドレスの入力（任意）
        mail_text = driver.find_element(By.ID, "email_single")
        mail_text.send_keys(email_address)

        # submit ボタンをクリック
        submit_btn = driver.find_element(
            By.XPATH, '//*[@id="singlePredictionForm"]/div/div[2]/div/div[1]/button')
        submit_btn.click()

        driver.implicitly_wait(10)

        cur_url = driver.current_url
        print(cur_url)
        cur_url = cur_url + "\n"

        fa = open(
            url_path, "a")
        fa.write(cur_url)
        fa.close()

        sleep(30)

driver.quit()
