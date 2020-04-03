from git import Repo
import os.path
from pathlib import Path

def install():
	
	# git url for Starcraft Replay Scanner
	git_url = "https://github.com/KaiJayaram/Starcraft-Replay-Scanner.git"
	print("Installing Starcraft Replay Scanner!")
	print("You can find more details about this project on my github here {}".format(git_url))

	# get user home
	home = str(Path.home())
	default_dir ="{}\\Documents\\Starcraft Replay Scanner".format(home)
	install_confirmed = False

	# find a good place to install
	while(not install_confirmed):
		print("Default installation directory: {}".format(default_dir))
		print("if this is okay type Y otherwise type your desired installation directory")

		install_dir = input()

		if install_dir.lower() == "y":
			install_dir = default_dir

		if os.path.exists(install_dir):
			print("{} already exists on this computer, still okay to install (Y/N)")
			user_response = input()
			if input.lower() == "y":
				Repo.clone_from(git_url, install_dir)
				install_confirmed = True
		else:
			Repo.clone_from(git_url, install_dir)
			install_confirmed = True

	# save installation directory in config file for updates
	with open("{}\\Starcraft Replay Scanner\\install_config.txt".format(install_dir), "w") as ic:
		ic.write("directory={}".format(install_dir))
		ic.write("\n")

def main():
	install()
	
if __name__ == '__main__':
    main()
