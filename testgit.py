import os
import yaml
import git
from git import Repo
import logging


def main():
	logging.basicConfig(filename='gittest.log',level=logging.DEBUG)
	if os.path.isdir("flux-demo"):
		g = git.cmd.Git("flux-demo")
		g.pull()
		logging.info('repo is pulled times')
	else:
		git.Git("").clone("git@github.com:itsmesinghavneet/flux-demo.git")
		logging.info('repo is cloned')

if __name__ == "__main__":main()	
	
def set_state(state):
    with open('flux-demo/hello-deploy.yaml') as f:
        doc = yaml.load(f)
        logging.debug('yaml file is loaded')
    doc['metadata']['annotations']['flux.weave.works/locked'] = state
    logging.debug('Selected the part to edit')
    with open('flux-demo/hello-deploy.yaml', 'w') as f:
	yaml.safe_dump(doc, f, default_flow_style=False)
	logging.debug('File is opened in write mode')	
set_state("true")
logging.debug('The value is changed ')
repo_dir = 'flux-demo/'
repo = Repo(repo_dir)
logging.debug('choosed the repo')
file_list = [
    'hello-deploy.yaml'
]
commit_message = 'deautomate'
logging.debug('The commit initialed')
repo.index.add(file_list)
logging.debug('File added')
repo.index.commit(commit_message)
origin = repo.remote('origin')
repo.git.push('git@github.com:itsmesinghavneet/flux-demo.git')
logging.debug('File is being pushed')
	
