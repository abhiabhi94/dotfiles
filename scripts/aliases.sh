# this file is used to store aliases useful for zsh shell
alias python="python3"
alias pip="python -m pip"

alias djtest="python manage.py test --keepdb"
alias djrun="python manage.py runserver"
alias djshell="python manage.py shell"
alias djmakemig="python manage.py makemigrations"
alias djmig="python manage.py migrate"
alias djcov="coverage run manage.py test --keepdb"

alias covrep="coverage report -m --skip-covered"
# force tmux to start with unicode(helps in displaying emoji)
alias tmux="tmux -u"

alias drun="docker run -it --rm ubuntu:latest bash"
alias comment="source /home/curious/.virtualenvs/comment/bin/activate"
