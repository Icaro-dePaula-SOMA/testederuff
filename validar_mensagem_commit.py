import re
import sys


def validar_mensagem(mensagem):
    padrao = r'^(feat|fix|docs|style|refactor|test|chore)(\([a-zA-Z0-9 _-]+\))?: .+$'
    return re.match(padrao, mensagem)


def main():
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, 'r', encoding='utf-8') as f:
        commit_msg = f.read().strip()

    if not validar_mensagem(commit_msg):
        print('[ERRO]: Mensagem de commit fora do padrão!')
        print("Use um formato como: 'tipo_do_commit(contexto): mensagem de commit'")
        sys.exit(1)


if __name__ == '__main__':
    main()
