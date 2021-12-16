from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pickle as p

base_url = "https://github.com/orgs/" 
base_sec = "/repositories?q=&type=&language=python&sort=stargazers"

paginated = "https://github.com/orgs/"
paginated_2 = "/repositories?language=python&page="
paginated_3 = "&q=&sort=stargazers&type="
repo_1 = "/html/body/div[4]/main/div/div/div[2]/div/div/div[2]/ul/li["
repo_2 = "]/div/div[1]/div[1]/h3/a"
# 'top' companies: Google, Facebook, Netflix, Microsoft, Amazon
# 'low' companies: ["att", "PTCInc","F5Networks", "zillow","Sentinel-One","factset","akamai","HewlettPackard","NetApp","splunk","ringcentral","confluentinc","wayfair","HubSpot", "Xilinx", "NVIDIA", "dell", "Verizon", "eBay"]
comps = ["nokia"]


starting_urls = [base_url + i + base_sec for i in comps]

driver = webdriver.Chrome(ChromeDriverManager().install())
comp_to_num = {}

for i in comps:
	url = base_url + i + base_sec
	driver.get(url)
	# Had weird errors when using this - I'm not a scraping expert but this seemed to do the trick
	try:
		num_res = driver.find_element_by_xpath("/html/body/div[4]/main/div/div/div[2]/div/div/div[1]/div[1]/strong[1]")
	except:
		print("Had to use 6")
		num_res = driver.find_element_by_xpath("/html/body/div[6]/main/div/div/div[2]/div/div/div[1]/div[1]/strong[1]")
	comp_to_num[i] = num_res.text
	print(i, num_res.text)
	break

comp_to_repo = {}

tot_search = 0
for comp, repos in comp_to_num.items():
	comp_to_repo[comp] = []
	print(comp, repos)
	page = 1
	first_url = paginated + comp + paginated_2 + str(page) + paginated_3
	driver.get(first_url)
	tot_search += 1
	for i in range(int(repos)):
		print(i, repos)
		if i % 30 == 0 and i != 0:
			page += 1
			new_url = paginated + comp + paginated_2 + str(page) + paginated_3
			driver.get(new_url)
			tot_search += 1
		li_num = i % 30 + 1
		elem_xpath = repo_1 + str(li_num) + repo_2
		#try:
		repo_elem = driver.find_element_by_xpath(elem_xpath)
		print(repo_elem.get_attribute('href'))
		comp_to_repo[comp].append(repo_elem.get_attribute('href').split("/")[-1])	
		
	print(comp_to_num)
	p.dump(comp_to_repo, open("bad_comp_repos/" + comp + "_to_repo.p", "wb"))
	break
