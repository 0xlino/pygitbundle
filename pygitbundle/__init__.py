import subprocess

MY_CUSTOM_VAR = 'my_custom_var'
MY_CUSTOM_VAR2 = 'my_custom_var2'

def create_bundle(bundle_file, repo_path):
    bundle_command = ['git', 'bundle', 'create', bundle_file, '--all']
    try:
        subprocess.run(bundle_command, cwd=repo_path, check=True)
        print('Git bundle created successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error creating Git bundle: {e.stderr.decode()}')

def verify_bundle(bundle_file, repo_path):
    verify_command = ['git', 'bundle', 'verify', bundle_file]
    try:
        subprocess.run(verify_command, cwd=repo_path, check=True)
        print('Git bundle verified successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error verifying Git bundle: {e.stderr.decode()}')

def unpack_bundle(bundle_file, repo_path):
    unpack_command = ['git', 'clone', bundle_file]
    try:
        subprocess.run(unpack_command, cwd=repo_path, check=True)
        print('Git bundle unpacked successfully.')
    except subprocess.CalledProcessError as e:
        print(f'Error unpacking Git bundle: {e.stderr}')
