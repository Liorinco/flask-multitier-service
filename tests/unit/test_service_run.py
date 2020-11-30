import os
import subprocess


def test_service_run_as_python_module():
    command = ["python", "-m", "service"]
    process = subprocess.Popen(
        args=command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        preexec_fn=os.setsid,
    )
    assert process.returncode is None, "The application does not run"
    process.terminate()
    output, error = process.communicate()
    assert process.returncode == -15  # 15: Unix SIGTERM
