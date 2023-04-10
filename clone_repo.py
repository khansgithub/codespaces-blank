import subprocess, os, pexpect

def subprocess_run(cmd, **kwargs):
    return subprocess.run(
        cmd.split(" "),
        check=True,
        stdout=subprocess.PIPE,
        **kwargs
    ).stdout.decode("utf-8")


def check_known_hosts():
    set_known_hosts = True
    try:
        # Replace this with `subprocess_run`
        keyscan = subprocess_run(
            "ssh-keygen -H -F main_db", check=True, stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
        if len(keyscan) > 1:
            set_known_hosts = False
            pass
    except Exception as err:
        pass

    if set_known_hosts:
        cmds = [
            "mkdir -p /root/.ssh",
            "touch /root/.ssh/known_hosts",
            f"ssh-keyscan {HOST}"
        ]
        process = None
        for c in cmds:
            try:
                # Replace this with `subprocess_run`
                process = subprocess_run(c, check=True, stdout=subprocess.PIPE)
            except subprocess.CalledProcessError as err:
                pass

        print(process)
        with open("/root/.ssh/known_hosts", 'a') as known_hosts:
            known_hosts.write(process.stdout.decode("utf-8"))
            known_hosts.write("\n")


HOST = subprocess_run("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' git")
REPO = "repo"
PORT = 3333
CLONE_TO = "./mod/"

if not os.path.isdir(os.path.join(os.getcwd(), CLONE_TO)):
    raise Exception(f"'{CLONE_TO}' does not exist in {os.getcwd()}")
check_known_hosts()

cmd = f"git clone --branch=master ssh://git@{HOST}:{PORT}/srv/{REPO} {CLONE_TO}"
child = pexpect.spawn(cmd, timeout=10)
child.expect("Cloning(.*)")
child.expect("git(.*)")
child.sendline('12345')
child.expect("Resolving deltas: 100%(.*)")
child.read()
