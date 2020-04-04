from git import Repo

# Install From github
def install(install_dir):	
	try:
		if(not install_dir.endswith("Starcraft Replay Scanner")):
			install_dir += "\\Starcraft Replay Scanner"
		# git url for Starcraft Replay Scanner
		git_url = "https://github.com/KaiJayaram/Starcraft-Replay-Scanner.git"
		Repo.clone_from(git_url, install_dir)
		return True
	except:
		return False

