from fabric.api import local, env, settings, abort, run, cd, prefix, sudo, prompt
from fabric.colors import green, red, yellow
from fabric.api import settings  # noqa
from contextlib import contextmanager as _contextmanager
from pyfiglet import Figlet

INIT = False

env.use_ssh_config = True
env.user = 'ubuntu'
env.hosts = ['159.89.166.117']
env.directory = '~/var/www/fractal_hackathon'
env.activate = 'source ~/var/www/fractal_hackathon/env/bin/activate'

APP_DIR = '~/var/www/fractal_hackathon/app'
STATIC_DIR = '{}/static'.format(APP_DIR)
SUPERVISOR_CONF = 'app'

figlet = Figlet(font='slant')

def _sudo_patch(*args, **kwargs):
    return sudo(*args, **kwargs)


_sudo = _sudo_patch


@_contextmanager
def _virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield


def set_requirements():
    run('pip install -r requirements.txt')


def _restart_app():
    with cd(APP_DIR):
        with _virtualenv():
            _sudo('supervisorctl restart {}'.format(SUPERVISOR_CONF))


def _setup_static():
    with cd(STATIC_DIR):
        run('yarn')
        run('node ./node_modules/webpack/bin/webpack.js -p')


def deploy():
    _confirm()
    with cd(APP_DIR):
        with _virtualenv():
            run('git pull origin master')
            set_requirements()
            _setup_static()
            _restart_app()


def _confirm():
    response = prompt("""
        type YES to continue to deploy ===>
        """)
    if response != "YES":
        abort(red("ABORTING DEPLOYMENT"))

    local("clear")
    print(green(figlet.renderText("LET'S GO...")))
