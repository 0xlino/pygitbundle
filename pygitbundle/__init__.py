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

