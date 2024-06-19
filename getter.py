import os
import requests
import yaml

url = '''https://api.github.com/repos/oscar-system/notebooks/contents'''
token = os.getenv("API_ACCESS_TOKEN")
headers = {"Authorization": f"Bearer {token}"}

#print(url)
#print(token)
#print(headers)

#r = requests.get(url=url, headers=headers)

#fyaml = r.content.decode('ascii')
fyaml = '''[{"name":"README.md","path":"README.md","sha":"11ba824e7ebe55040e5518e51e8c78e339225f72","size":11,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/README.md?ref=master","html_url":"https://github.com/oscar-system/notebooks/blob/master/README.md","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/11ba824e7ebe55040e5518e51e8c78e339225f72","download_url":"https://raw.githubusercontent.com/oscar-system/notebooks/master/README.md?token=ABY3USB2BXGSORCV76Q6Q53GOKKWY","type":"file","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/README.md?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/blobs/11ba824e7ebe55040e5518e51e8c78e339225f72","html":"https://github.com/oscar-system/notebooks/blob/master/README.md"}},{"name":"combinatorics","path":"combinatorics","sha":"c663c4fafc749723eddd4a9d068696bcc46f0c1f","size":0,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics?ref=master","html_url":"https://github.com/oscar-system/notebooks/tree/master/combinatorics","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/trees/c663c4fafc749723eddd4a9d068696bcc46f0c1f","download_url":null,"type":"dir","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/combinatorics?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/trees/c663c4fafc749723eddd4a9d068696bcc46f0c1f","html":"https://github.com/oscar-system/notebooks/tree/master/combinatorics"}},{"name":"galois_cohomology","path":"galois_cohomology","sha":"f0120ee42d79d5b163706e7d29177d0de58226c2","size":0,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/galois_cohomology?ref=master","html_url":"https://github.com/oscar-system/notebooks/tree/master/galois_cohomology","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/trees/f0120ee42d79d5b163706e7d29177d0de58226c2","download_url":null,"type":"dir","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/galois_cohomology?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/trees/f0120ee42d79d5b163706e7d29177d0de58226c2","html":"https://github.com/oscar-system/notebooks/tree/master/galois_cohomology"}},{"name":"galois_meets_ehrhart","path":"galois_meets_ehrhart","sha":"0514756e19c01bdc4258787ebd825258191c377c","size":0,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/galois_meets_ehrhart?ref=master","html_url":"https://github.com/oscar-system/notebooks/tree/master/galois_meets_ehrhart","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/trees/0514756e19c01bdc4258787ebd825258191c377c","download_url":null,"type":"dir","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/galois_meets_ehrhart?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/trees/0514756e19c01bdc4258787ebd825258191c377c","html":"https://github.com/oscar-system/notebooks/tree/master/galois_meets_ehrhart"}},{"name":"triangle_group","path":"triangle_group","sha":"f4eb1d7abcf4f2aee2cbb75ed5c6aa6af4730151","size":0,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/triangle_group?ref=master","html_url":"https://github.com/oscar-system/notebooks/tree/master/triangle_group","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/trees/f4eb1d7abcf4f2aee2cbb75ed5c6aa6af4730151","download_url":null,"type":"dir","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/triangle_group?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/trees/f4eb1d7abcf4f2aee2cbb75ed5c6aa6af4730151","html":"https://github.com/oscar-system/notebooks/tree/master/triangle_group"}},{"name":"tropical_grassmannian","path":"tropical_grassmannian","sha":"12b9faa7aa6df94ace9cf07b2800a63ac7224e5a","size":0,"url":"https://api.github.com/repos/oscar-system/notebooks/contents/tropical_grassmannian?ref=master","html_url":"https://github.com/oscar-system/notebooks/tree/master/tropical_grassmannian","git_url":"https://api.github.com/repos/oscar-system/notebooks/git/trees/12b9faa7aa6df94ace9cf07b2800a63ac7224e5a","download_url":null,"type":"dir","_links":{"self":"https://api.github.com/repos/oscar-system/notebooks/contents/tropical_grassmannian?ref=master","git":"https://api.github.com/repos/oscar-system/notebooks/git/trees/12b9faa7aa6df94ace9cf07b2800a63ac7224e5a","html":"https://github.com/oscar-system/notebooks/tree/master/tropical_grassmannian"}}]'''
fyamlcontent = yaml.safe_load(fyaml)

outstring = ""

for i in fyamlcontent:
    if i["type"] == "dir":
        outstring += f"""'{i["name"]} {i["url"]}', """
        # just send the URL to tester.py

outstring = outstring[0:-2]
print(outstring)