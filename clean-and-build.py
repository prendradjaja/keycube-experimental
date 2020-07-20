import os

REMOTE = 'https://github.com/prendradjaja/keycube.git'
THIS_REPO_NAME = 'keycube-experimental'

os.system('rm -rf x')

indexhtml = ''

for line in open('branches'):
    branch = line.strip()
    directory = 'x/' + branch
    os.system(
        'git clone --single-branch --branch ' +
        branch + ' ' +
        REMOTE + ' ' +
        directory
    ) and exit()  # Exit if failed
    os.system('rm -rf '+directory+'/.git')
    href = '/'+THIS_REPO_NAME+'/'+directory
    indexhtml += '<a href="'+href+'">'+branch+'</a><br>\n'

with open('index.html', 'w') as index:
    index.write(indexhtml)

print('Done.')
