import subprocess

def run_helm_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode().strip()}")
        return None
    return output.decode().strip()

def install_umbrella_chart(release_name, chart_path):
    return run_helm_command(f"helm install {release_name} {chart_path}")

if __name__ == "__main__":
    print(install_umbrella_chart('dune-sand-release', './dune-sand'))
