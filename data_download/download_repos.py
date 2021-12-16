import os
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import pickle as p

base_url = "https://github.com/" 

# 'top' companies: Google, Facebook, Netflix, Microsoft, Amazon
# 'low' companies: ["att", "PTCInc","F5Networks", "zillow","Sentinel-One","factset","akamai","HewlettPackard","NetApp","splunk","ringcentral","confluentinc","wayfair","HubSpot", "Xilinx", "NVIDIA", "dell", "Verizon", "eBay"]
comps = ["nokia"]
comps_to_repos = {}
for i in comps:
	p_file = i + "_to_repo.p"
	a = p.load(open("bad_comp_repos/" + p_file, "rb"))
	comps_to_repos[i] = a[i]

driver = webdriver.Chrome(ChromeDriverManager().install())

for comp, repos in comps_to_repos.items():
	for repo in repos:
		done = os.listdir("/Users/Mack/cs_334_dataset/bad_zipped_repos")
		already_done = False
		for x in done:
			if x[:-11] == repo:
				already_done = True
		if already_done:
			print("Already done: ", repo)
			continue
		print("Now doing: ", repo)
		driver.get("https://github.com/" + comp + "/" + repo)
		try:
			to_click = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[1]/span/get-repo/details/summary")
			to_click.click()
			time.sleep(1)
			to_download = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[1]/span/get-repo/details/div/div/div[1]/ul/li[3]/a")
			to_download.click()
		except:
			continue
		f = False
		tries = 0
		# This is a hacky way to wait for the download to finish and rename any possible main branches
		while f == False:
			try:
				tries += 1
				os.replace("/Users/Mack/Downloads/" + repo + "-master.zip", "/Users/Mack/cs_334_dataset/bad_zipped_repos/" + repo + "-master.zip")
				f = True
			except:
				try:
					os.replace("/Users/Mack/Downloads/" + repo + "-main.zip", "/Users/Mack/cs_334_dataset/bad_zipped_repos/" + repo + "-master.zip")
					f = True
				except:
					try:
						os.replace("/Users/Mack/Downloads/" + repo + "-dev.zip", "/Users/Mack/cs_334_dataset/bad_zipped_repos/" + repo + "-master.zip")
						f = True
					except:
						try:
							os.replace("/Users/Mack/Downloads/" + repo + "-develop.zip", "/Users/Mack/cs_334_dataset/bad_zipped_repos/" + repo + "-master.zip")
							f = True
						except:
							if tries > 15:
								f = True
							else:
								time.sleep(1)
	break
