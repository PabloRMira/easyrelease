# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/04_utils.ipynb (unless otherwise specified).

__all__ = ['check_git_dir', 'check_project_root', 'read_credentials', 'get_config', 'get_template', 'update_gitignore',
           'write_settings_ini', 'write_setup_py', 'write_conda_build_scripts', 'get_conda_env_packages',
           'get_anaconda_credentials', 'get_pypi_credentials', 'write_init_version', 'run_tests']

# Cell
import os
import re
import functools
import tempfile
import pkgutil
import subprocess
from configparser import ConfigParser

# Cell
def check_git_dir():
    "Check whether there is a .git directory in your current folder"
    return bool(os.path.exists(".git"))

# Cell
def check_project_root(func):
    """Check that the user is on the project root directory by checking if there is a .git folder
    before running `func`
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not check_git_dir():
            raise Exception("You need to be on your project root to execute this command")
        else:
            return func(*args, **kwargs)
    return wrapper

# Cell
@check_project_root
def read_credentials(path):
    "Read credentials from `path`"
    config = ConfigParser(delimiters=['='])
    with open(path, "r") as f:
        config.read_string("[DEFAULT]\n" + f.read())
    return config["DEFAULT"]

# Cell
def get_config():
    "Get config from settings.ini"
    config = ConfigParser(delimiters=['='])
    config.read('settings.ini')
    cfg = config['DEFAULT']
    return cfg

# Cell
def get_template(name):
    "Get template with filename `name`"
    template = pkgutil.get_data(__name__, f"templates/{name}").decode("utf-8")
    return template

# Cell
@check_project_root
def update_gitignore():
    "Update .gitignore with stuff we do not want to track"
    print("Updating .gitignore")
    add_ignore_files = [
        ".gh-credentials",
        "conda-recipe/*",
        "conda-bld/*",

    ]
    if os.path.exists(".gitignore"):
        with open(".gitignore", "r") as f:
            ignore_files = f.read().split("\n")
        for ifile in add_ignore_files:
            if ifile not in ignore_files:
                ignore_files.append(ifile)
        ignore_file = "\n".join(ignore_files)
    else:
        ignore_file = "\n"
    with open(".gitignore", "w") as f:
        f.write(ignore_file)

# Cell
@check_project_root
def write_settings_ini(project_type):
    "Write settings.ini from template"
    print("Generating settings.ini")
    if os.path.exists("settings.ini"):
        print("settings.ini already exists. Skipping this step")
    else:
        temp_name = "settings_template.ini" if project_type == "package" else "settings_slim_template.ini"
        template = get_template(temp_name)
        with open("settings.ini") as f:
            f.write(template)

# Cell
@check_project_root
def write_setup_py():
    "Write setup.py from template"
    print("Generating setup.py")
    if os.path.exists("setup.py"):
        print("setup.py already exists. Skipping this step")
    else:
        template = get_template("setup_template.py")
        with open("setup.py") as f:
            f.write(template)

# Cell
@check_project_root
def write_conda_build_scripts():
    "Write bld.bat and build.sh scripts for building conda packages"
    "Generating bld.bat and build.sh for conda recipe"
    if not os.path.exists("conda-recipe"):
        os.mkdir("conda-recipe")
    temp_map = {
        "bld.bat": "bld_template.bat",
        "build.sh": "build_template.sh"
    }
    for file_name, temp_name in temp_map.items():
        print(f"Generating file {file_name}")
        if os.path.exists(os.path.join("conda-recipe", file_name)):
            print(f"{file_name} already exists. Skipping this step")
        else:
            template = get_template(temp_name)
            with open(os.path.join("conda-recipe", file_name), "w") as f:
                f.write(template)

# Cell
def get_conda_env_packages():
    "Get conda environment packages"
    packages = subprocess.run(["conda", "list", "--explicit"], capture_output=True).stdout.decode("utf").splitlines()
    packages = [p for p in packages if not re.match(r"^(?:#|@)", p) and not re.search("dev", p.split("=")[-1])]
    return packages

# Cell
@check_project_root
def get_anaconda_credentials():
    "Get anaconda credentials from .anaconda-credentials in your home or project root directory"
    ana_file = ".anaconda-credentials"
    user_root = os.path.expanduser("~")
    if os.path.exists(ana_file):
        cfg = read_credentials(ana_file)
    elif os.path.exists(os.path.join(user_root, ana_file)):
        cfg = read_credentials(os.path.join(user_root, ana_file))
    else:
        raise Exception(
            "No .anaconda-credentials file found. "
            "Please save your anaconda credentials "
            "either in this project's root directory or under your home directory"
        )
    return (cfg["username"], cfg["password"])

# Cell
@check_project_root
def get_pypi_credentials():
    "Get pypi credentials from .pypi-credentials in your home or project root directory"
    pypi_file = ".pypi-credentials"
    user_root = os.path.expanduser("~")
    if os.path.exists(pypi_file):
        cfg = read_credentials(pypi_file)
    elif os.path.exists(os.path.join(user_root, pypi_file)):
        cfg = read_credentials(os.path.join(user_root, pypi_file))
    else:
        raise Exception(
            "No .pypi-credentials file found. "
            "Please save your pypi credentials "
            "either in this project's root directory or under your home directory"
        )
    return (cfg["username"], cfg["password"])

# Cell
def write_init_version():
    "Write __version__ in __init__.py if it is a package"
    cfg = get_config()
    if "lib_name" in cfg:
        package_name = cfg["lib_name"]
        version = cfg["version"]
        if os.path.exists(package_name):
            init_path = os.path.join(package_name, "__init__.py")
            if not os.path.exists(init_path):
                print("No __init__.py file found. Generating it")
                with open(init_path, "w") as f:
                    f.write(f'__version__ = "{version}"')
            else:
                with open(init_path, "r") as f:
                    init_lines = f.readlines()
                has_version = max([True if "__version__" in line else False for line in init_lines])
                if has_version:
                    print("Updating __version__ in __ini__.py")
                    update_init_lines = [
                        re.sub(r'__version__ = ".*"', f'__version__ = "{version}"', line)
                        for line in init_lines
                    ]
                else:
                    update_init_lines += [f'\n__version__ = "version"']
                update_init = "".join(update_init_lines)
                with open(init_path, "w") as f:
                    f.write(update_init)

# Cell
def run_tests(func):
    "Run pytest or nbdev_test_nbs before calling function"
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        cfg = get_config()
        if os.path.exists("tests"):
            print("Running pytests")
            exit_code = subprocess.run(["pytest", "tests"]).returncode
        elif "lib_name" in cfg:
            package_name = cfg["lib_name"]
            nbdev_file = os.path.join(package_name, "_nbdev.py")
            if os.path.exists(nbdev_file):
                print("Running nbdev_test_nbs")
                exit_code = subprocess.run(["nbdev_test_nbs"]).returncode
        else:
            print("Neither tests folder nor nbdev project found. Skipping tests")
            exit_code = 0
        if exit_code != 0:
            raise Exception("Tests failed! Aborting next steps")
        return func(*args, **kwargs)
    return wrapper