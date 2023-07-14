# !pip3 install -U selenium
# !pip3 install -U webdriver_manager
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # locate elements
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


# TODO
protein = "5uwc_binary"
trj_num = "trj02"
wildtype_residue = "W 397  (TRP)"
mutant_residue = "K"

mutation_chain = "B"
email_addres = "20a1004c@shinshu-u.ac.jp"


urllist = []

# url保存ファイルの作成
fw = open(f"/mnt/c/users/komad/documents/url_result/beatmusic/{protein}/beatmusic_url_{protein}_{trj_num}.txt", 'w')
fw.write('')
fw.close()

driver = webdriver.Chrome(ChromeDriverManager().install())


for i in range(20):

    run_num = i + 3

    driver.get('http://babylone.ulb.ac.be/beatmusic')

    play_button = driver.find_element(By.XPATH, '//html/body/center/center[1]/a[1]/img')
    play_button.click()
    # 読み込まれるまで待機
    sleep(1)
    # WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS, 'input')))


    print (f"run{run_num}")
    # file_path = f"/mnt/c/users/komad/desktop/5uv8_binary/{trj_num}/edit_run{run_num}.pdb"
    file_path  = f"/mnt/c/users/komad/documents/editpdb/{protein}/{trj_num}/edit_run{run_num}.pdb"
    upload_input = driver.find_element(By.NAME, "pdbfile")
    upload_input.send_keys(file_path)


    # submit ボタンをクリック
    submit_btn_1 = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/form/table/tbody/tr[2]/td/input[1]')
    submit_btn_1.click()
    # 読み込まれるまで待機
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'target_tab1')))

    # パートナー1を選択
    chain_a = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[6]/input')
    chain_a.click()

    # パートナー2を選択
    chain_b = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[11]/input')
    chain_b.click()

    # いらない鎖を選択
    discard = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[16]/input')
    discard.click()

    # submit ボタンをクリック
    submit_btn_2 = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[3]/td/input')
    submit_btn_2.click()
    # 読み込まれるまで待機
    sleep(1)

    # 変異残基を指定するラジオボタンをクリック
    radio_button = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[1]/td/input[2]')
    radio_button.click()
 
    # 変異を入れる鎖の指定
    chain_button = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[4]/select')
    chain_button.click()
    
    chain_button_d = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[4]/select/option[3]')
    chain_button_d.click()

    # ミスセンス変異を入れるアミノ酸残基を指定
    wt_button = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[5]/select')
    wt_button.click()
    
    wt_button_d = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[5]/select/option[107]')
    wt_button_d.click()

    # 変異先のアミノ酸を指定
    mt_button = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[6]/select')
    mt_button.click()
    
    mt_button_d = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[2]/td/div[6]/select/option[10]')
    mt_button_d.click()

    # submit ボタンをクリック
    submit_btn = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/center/form/table/tbody/tr[3]/td/input')
    submit_btn.click()
    # 読み込まれるまで待機
    sleep(1)

    result_url = driver.find_element(By.XPATH, '/html/body/center/center[2]/table/tbody/tr/td/center/a')
    result_url_text = result_url.text
    # print(result_url_text)
    urllist.append(result_url_text)
    result_url_text = result_url_text + "\n"

    fa = open(f"/mnt/c/users/komad/documents/url_result/beatmusic/{protein}/beatmusic_url_{protein}_{trj_num}.txt","a" )
    fa.write(result_url_text)
    fa.close()

    sleep(1)

driver.quit()



print(f"protein: {protein}, trj_num: {trj_num}, chain: {mutation_chain}\n{wildtype_residue} -> {mutant_residue}")

num = len(urllist)
for i in range(num):
    print(urllist[i])
