import os
import sys
import yaml
import base64
import requests
import subprocess

print(sys.argv)

def grab_file(filelink, token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get(url=filelink, headers=headers)
    #print(r.content.decode('ascii'))
    fyaml = r.content.decode()
    fyaml = yaml.safe_load(fyaml)
    with open(fyaml["name"], 'w') as writefile:
        writefile.write(base64.b64decode(fyaml['content']).decode('utf8'))


name = sys.argv[1]
dirlink = sys.argv[2]
token = os.getenv("API_ACCESS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

r = requests.get(url=dirlink, headers=headers)
ryaml = r.content.decode('ascii')

#ryaml = '''[{"name":"DemoCombinatorics.ipynb","path":"combinatorics/DemoCombinatorics.ipynb","sha":"e79937261893b94eef9cee5d9e0795b85279af5b","size":27805,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/DemoCombinatorics.ipynb?ref=master","html_url":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/DemoCombinatorics.ipynb","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/e79937261893b94eef9cee5d9e0795b85279af5b","download_url":"https://raw.githubusercontent.com/oscar-system/notebooks/master/combinatorics/DemoCombinatorics.ipynb?token=ABY3USEGBIFPBWWJHFN2IITGOLEF2","type":"file","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/DemoCombinatorics.ipynb?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/e79937261893b94eef9cee5d9e0795b85279af5b","html":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/DemoCombinatorics.ipynb"}},{"name":"Project.toml","path":"combinatorics/Project.toml","sha":"88e9a0d4093595cf7dc10557f0b04ac067731781","size":54,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/Project.toml?ref=master","html_url":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/Project.toml","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/88e9a0d4093595cf7dc10557f0b04ac067731781","download_url":"https://raw.githubusercontent.com/oscar-system/notebooks/master/combinatorics/Project.toml?token=ABY3USAI256CTT43YONR5FLGOLEF2","type":"file","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/Project.toml?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/88e9a0d4093595cf7dc10557f0b04ac067731781","html":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/Project.toml"}},{"name":"README.md","path":"combinatorics/README.md","sha":"60bb57738309e60966978a9c8bad2979fe12838b","size":57,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/README.md?ref=master","html_url":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/README.md","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/60bb57738309e60966978a9c8bad2979fe12838b","download_url":"https://raw.githubusercontent.com/oscar-system/notebooks/master/combinatorics/README.md?token=ABY3USD2UTXMJFOYCQXZSTTGOLEF2","type":"file","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics/README.md?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/60bb57738309e60966978a9c8bad2979fe12838b","html":"https://github.com/oscar-system/notebooks/blob/master/combinatorics/README.md"}}]'''
ryaml = yaml.safe_load(ryaml)
#print(ryaml[0]["url"])

nbfilename = ''

for i in ryaml:
    if "ipynb" in i["name"]:
        nbfilename = i["name"]
    grab_file(i["url"], token)

#init julia depot
os.environ['JULIA_PROJECT'] = os.getcwd()
subprocess.run('''julia -e "using Pkg; Pkg.instantiate()"''', shell=True, check=True)

#finally run the stuff
if nbfilename == '':
    raise AssertionError("cant be empty")
subprocess.run(f'''jupytext --set-kernel "julia-1.10" --execute {nbfilename}''', shell=True, check=True)