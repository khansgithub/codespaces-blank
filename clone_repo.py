import subprocess, os

def subprocess_run(cmd, **kwargs):
    return subprocess.run(
        cmd.split(" "),
        check=True,
        stdout=subprocess.PIPE,
        **kwargs
    ).stdout.decode("utf-8")

folder_name = "mod"
if not os.path.isdir(os.path.join(os.getcwd(), folder_name)):
    raise Exception(f"'{folder_name}' does not exist in {os.getcwd()}")


HOST = subprocess_run("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' git")
PORT = 3333
PATH = "/clone_dir/"
cmd = f"git clone --branch=master ssh://git@{HOST}:{PORT}/srv/git/{folder_name} {PATH}"

subprocess_run(cmd)
