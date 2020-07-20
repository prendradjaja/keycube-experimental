import os

remote = 'https://github.com/prendradjaja/keycube.git'

os.system('rm -rf x')

indexhtml = ''

for line in open('branches'):
    branch = line.strip()
    directory = 'x/' + branch
    os.system(
        'git clone --single-branch --branch ' +
        branch + ' ' +
        remote + ' ' +
        directory
    )
    os.system('rm -rf '+directory+'/.git')
    indexhtml += '<a href="/'+directory+'">'+branch+'</a><br>\n'

with open('index.html', 'w') as index:
    index.write(indexhtml)

print('Done.')
