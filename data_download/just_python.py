import subprocess
import os

curr_dir = "/Users/Mack/cs_334_dataset/"
target_dir = "bad_python_files"
zipped_repos = "test_repos"

first = "yes | unzip "
second = "yes | find "
sec_2 = " -mindepth 2 -type f -exec mv -i '{}' "
sec_3 = " ';'" 

print("before unzip")
for zr in os.listdir(curr_dir + zipped_repos):
	bash_one = first + zr
	zr = zr[:-4]
	process = subprocess.run(bash_one, cwd = curr_dir + zipped_repos, shell = True)
	print(process)

print("after unzip")
bash_two = "yes | rm *.zip"
process = subprocess.run(bash_two, cwd = curr_dir + zipped_repos, shell = True)
print(process)

for zr in os.listdir(curr_dir + zipped_repos):
	bash_two = second + zr + sec_2 + zr + sec_3
	print(bash_two)
	process = subprocess.run(bash_two, cwd = curr_dir + zipped_repos, shell = True)
	print(process)
	bash_three = "yes | mv " + zr + "/*.py ../" + target_dir + "/"
	process = subprocess.run(bash_three, cwd = curr_dir + zipped_repos, shell = True)
	print(process)
	bash_four = "yes | rm -r " + zr
	process = subprocess.run(bash_four, cwd = curr_dir + zipped_repos, shell = True)
