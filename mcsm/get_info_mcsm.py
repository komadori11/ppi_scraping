import requests
from bs4 import BeautifulSoup as bs

# TODO
protein = "5uwc"
num = 10
# process = "process"
process = "min_process"

# 初期表示用
print("++++++++++++++++++++++")
print(f" protein : {protein}")
print(f" trajectory : {num}")
print(f" process : {process}")
print("++++++++++++++++++++++")
print("")

error = 0
for i in range(num):
    tn = i+1
    if (tn < 10):
        trj_num = f"trj0{tn}"
    else:
        trj_num = f"trj{tn}"

    print(protein + ": " + trj_num)

    url_path = f"/home/komadori/documents/ppi_scr_v2/result/mcsm/url/{protein}/{process}/mcsm_url_{protein}_{trj_num}.txt"
    result_path = f"/home/komadori/documents/ppi_scr_v2/result/mcsm/delta_g/{protein}/mcsm_{process}_{protein}_{trj_num}.txt"

    fw = open(result_path, "w")
    fw.write("")
    fw.close()

    with open(url_path) as f:
        lines = f.readlines()

    size = len(lines)
    print(f"size: {size}")

    for j in range(size):
        lines[j] = lines[j].replace('\n', '')

    for i in range(size):
        url = lines[i]
        res_mcsm = requests.get(url)
        soup_mcsm = bs(res_mcsm.text, 'html.parser')
        pred = soup_mcsm.find(id='ppi2Prediction')
        if (pred is None):
            print("ERROR")
            error = error+1
        else:
            result = pred.text
            print(result)

            fa = open(result_path, "a")
            result = result + "\n"
            fa.write(result)
            fa.close()

# 結果表示
print("")
print("++++++++++++++++++++++")
print(f"protein : {protein}")
print(f"trajectory : {num}")
print(f"process : {process}")
print(f"ERROR : {error}")
print("++++++++++++++++++++++")
print(
    """
 _______________
< All completed >
 ---------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
""")
