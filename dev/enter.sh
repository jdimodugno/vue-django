. env/bin/activate

mkdir -p /tmp/img

export MEDIA_ROOT='/tmp/'
export MEDIA_URL='img/'

alias serve='make run';
alias migrations='python ./manage makemigrations backend'
alias migrationsall='python ./manage makemigrations'
alias migrateall='python ./manage migrate'
alias migrate='python ./manage migrate backend'
alias shell='python ./manage shell_plus'
alias createuser='python ./manage createsuperuser'
