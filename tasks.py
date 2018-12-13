from invoke import task

TEST_PATH = "./tests"


@task
def build(c):
    print("Building!")


@task
def test(c):
    print("Testing")
    c.run("pipenv run python -m pytest --verbose --color=yes {}".format(TEST_PATH))


@task
def init(c):
    print("Initializing")
    c.run("pipenv install")


@task
def run(c):
    c.run("pipenv run python lyrics/app.py")
