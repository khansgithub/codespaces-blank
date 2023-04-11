import subprocess


class Main():
    def run(self):
        self.install_requirements()
        import afkak
        return afkak.CODEC_GZIP

    def install_requirements(self):
        result = subprocess.run(
            ["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception("Could not perform pip install")

