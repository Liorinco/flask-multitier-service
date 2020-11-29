import subprocess


def test_service_run_as_python_module():
    process_result = subprocess.run(["python", "-m", "service"])
    assert process_result.returncode == 0
