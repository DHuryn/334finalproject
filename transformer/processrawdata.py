
import os
import csv
path = "good_python_files"
os.chdir(path)
  
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
cs = open("good.csv", "w", newline='')
writer = csv.writer(cs, delimiter='|')
writer.writerow(["label", "text"])
# iterate through all files in the directory
count=0
for file in os.listdir():
    if file.endswith(".py"):
        file_path = f"{file}"
        with open(file_path, 'r') as f:
            try:
                s = f.read()
                if '|' in s or '|' in s:
                    continue
                li = ['amazon','google','netflix','microsoft','facebook']
                for lis in li:
                    s=s.replace(lis,'').replace(lis.upper(),'').replace(lis[0].upper()+lis[1:],'')
                writer.writerow([1, s ])
               # print(1)
            except:
                count += 1
    cs.flush()
path = "bad_python_files"
os.chdir('..')
os.chdir(path)

count=0
for file in os.listdir():
    if file.endswith(".py"):
        file_path = f"{file}"
        with open(file_path, 'r') as f:
            try:
                s = f.read()
                if '|' in s:
                    continue
                li = ["att", "ptcinc","f5networks", "zillow","sentinel-one","factset","akamai","hewlettpackard","netapp","splunk","ringcentral","confluentinc","wayfair","hubspot", "xilinx", "nvidia", "dell", "verizon", "ebay"]
                for lis in li:
                    s=s.replace(lis,'').replace(lis.upper(),'').replace(lis[0].upper()+lis[1:],'')
                writer.writerow([0, s ])
               # print(1)
            except:
                count += 1
    cs.flush()
path = "bad_python_files"
os.chdir('..')
os.chdir(path)

cs.close()
print(count)
