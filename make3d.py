import os
import shutil
from textwrap import dedent
import argparse
import subprocess

parser = argparse.ArgumentParser(description='This is a script to create 3D model folder structure')
parser.add_argument('-p', '--project', help='3D project name', required=True)
parser.add_argument('-wd', '--wd', help='Working directory', required=True)
args = parser.parse_args()

os.chdir(args.wd)

root_dir = os.path.join(args.wd, args.project)

if os.path.exists(root_dir) and os.listdir(root_dir):
    # If the path already exists and it is not empty, raise an error
    err_msg = '''
            {directory} already exists and it is not empty.

            Please try a different project name or root directory.

            '''.format(directory=root_dir)
    raise IOError(000, dedent(err_msg))
else:
    os.mkdir(root_dir)  # Create the root directory

dirnames = ('images', 'masks', 'models')
# Create all the other directories
for item in dirnames:
    path3D = os.path.join(args.wd, args.project, item)
    os.mkdir(path3D)


def write_readme(project, root_dir):
    readme_path = os.path.join(root_dir, "README.md")
    readme_content = get_readme_text(project)
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_content)


def get_readme_text(project):
    readme_text = """
        # {project}
        3D data for recreation of a British Museum object.
        # LICENSE
        The contents of this repository are licensed under CC-BY-NC-SA
        # Credits
        Photographs and models by {author} <{author_email}>, Digital Humanities Lead, British Museum
    """.format(
        project=project,
        license=license,
        author=get_user_name_from_git() or "My Name",
        author_email=get_user_email_from_git() or "My email.")
    return dedent(readme_text)


def get_user_name_from_git():
    try:
        git_process = subprocess.Popen(['git', 'config', 'user.name'], stdout=subprocess.PIPE
                                       , stderr=subprocess.PIPE)
        user_name, err = git_process.communicate()
        return user_name.rstrip().decode()
    except OSError:
        return None


def get_user_email_from_git():
    try:
        git_process = subprocess.Popen(['git', 'config', 'user.email'], stdout=subprocess.PIPE
                                       , stderr=subprocess.PIPE)
        user_email, err = git_process.communicate()
        return user_email.rstrip().decode()
    except OSError:
        return None


def write_license(root_dir):
    license_path = os.path.join(root_dir, "LICENSE.md")
    shutil.copy(os.path.join(os.path.dirname(os.path.realpath(__file__)),'scaffold3D/templates/LICENSE.md'), license_path)
    return None

def write_ignore(root_dir):
    ignore_path = os.path.join(root_dir, ".gitignore")
    shutil.copy(os.path.join(os.path.dirname(os.path.realpath(__file__)),'scaffold3D/templates/.gitignore'), ignore_path)
    return None


write_readme(args.project, root_dir)
write_license(root_dir)
write_ignore(root_dir)
