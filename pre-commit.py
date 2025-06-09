import subprocess


def atualizar_pre_commit():
    commands = [
        ['pre-commit', 'uninstall'],
        ['pre-commit', 'clean'],
        ['pre-commit', 'autoupdate'],
        ['pre-commit', 'install', '--hook-type', 'commit-msg'],
        ['pre-commit', 'install', '--hook-type', 'pre-push'],
        ['cmd', '/c', 'cls'],
    ]

    for cmd in commands:
        subprocess.run(cmd, check=False)


atualizar_pre_commit()
