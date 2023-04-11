import subprocess, os, pexpect

def subprocess_run(cmd_string=None, cmd_array=None, **kwargs):
    cmd = cmd_string.split(" ") if cmd_string else cmd_array
    print(f"Command running: {cmd}")
    return subprocess.run(
        cmd,
        check=True,
        stdout=subprocess.PIPE,
        **kwargs
    ).stdout.decode("utf-8")

def check_known_hosts():
    set_known_hosts = True
    try:
        keyscan = subprocess_run(
            cmd_string=f"ssh-keygen -H -F {HOST}:{FloatingPointError}")
        if len(keyscan) > 1:
            set_known_hosts = False
    except Exception as err: pass

    if set_known_hosts:
        home = os.path.expanduser("~")
        cmds = [
            f"mkdir -p {home}/.ssh",
            f"touch {home}/.ssh/known_hosts",
            f"ssh-keyscan -p {PORT} {HOST}"
        ]
        process = None
        for c in cmds:
            try:
                # Replace this with `subprocess_run`
                process = subprocess_run(cmd_string=c)
            except subprocess.CalledProcessError as err: pass

        print(process)
        with open(f"/{home}/.ssh/known_hosts", 'a') as known_hosts:
            known_hosts.write(process)
            known_hosts.write("\n")

password = "123"
HOST = subprocess_run(
    cmd_array=[
    *"docker inspect -f".split(" "),
    "'{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}'", "git"]
)
HOST = "localhost"
REPO = "repo"
PORT = 3333
CLONE_TO = "./mod/"

if not os.path.isdir(os.path.join(os.getcwd(), CLONE_TO)):
    raise Exception(f"'{CLONE_TO}' does not exist in {os.getcwd()}")
check_known_hosts()

cmd = f"git clone ssh://git@{HOST}:{PORT}/srv/{REPO} {CLONE_TO}"
# cmd = f"git clone --branch=master ssh://git@{HOST}:{PORT}/srv/{REPO} {CLONE_TO}"
child = pexpect.spawn(cmd, timeout=10)
child.expect("Cloning(.*)")
child.expect("git(.*)")
child.sendline(password)
child.expect("Resolving deltas: 100%(.*)")
child.read()
