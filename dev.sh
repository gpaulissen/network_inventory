#!/usr/bin/env bash

run () {
    setup
    find . -name __pycache__ -o -name "*.pyc" -delete
    sudo iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
    overmind start
}

setup () {
    overmind start -l db -D
    if [ -f .direnv/first_run ]; then
        sleep 2
        python ./src/manage.py collectstatic --noinput
        python ./src/manage.py makemigrations
        python ./src/manage.py migrate
    else
        python ./src/manage.py collectstatic --noinput
        python ./src/manage.py makemigrations backups
        python ./src/manage.py makemigrations computers
        python ./src/manage.py makemigrations core
        python ./src/manage.py makemigrations customers
        python ./src/manage.py makemigrations devices
        python ./src/manage.py makemigrations licenses
        python ./src/manage.py makemigrations nets
        python ./src/manage.py makemigrations softwares
        python ./src/manage.py makemigrations users
        python ./src/manage.py makemigrations
        python ./src/manage.py migrate
        python ./src/manage.py loaddata backups
        python ./src/manage.py loaddata computers
        python ./src/manage.py loaddata core
        python ./src/manage.py loaddata devices
        python ./src/manage.py loaddata nets
        python ./src/manage.py loaddata softwares
        python ./src/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
        init
        touch .direnv/first_run
    fi
    overmind quit

}

venv () {
    nix build .#venv -o .venv
}

docker (){
    nix build && docker load < result && docker run --rm -ti network-inventory:latest
}

clean () {
    find . \( -name __pycache__ -o -name "*.pyc" \) -delete
    rm -rf htmlcov/
    rm -f .direnv/first_run
    rm -f src/*/migrations/0*.py
    rm -rf .direnv/postgres/
}

cleanall () {
    git clean -xdf
}

init () {
    python ./src/manage.py loaddata src/network_inventory.yaml
}

debug () {
    pytest --pdb --nomigrations --cov=. --cov-report=html ./src/
}

check (){
    nix flake check
}

test (){
    export DJANGO_SETTINGS_MODULE=network_inventory.settings.ram_test
    pytest -nauto --nomigrations --cov-config="$PROJECT_DIR/.coveragerc" --cov-report=html "$PROJECT_DIR/src"
}

update (){
    poetry update --lock
}

tasks=("check" "clean" "cleanall" "debug" "docker" "run" "test" "update" "venv")

# only one task at a time
if [ $# != 1 ]; then
    echo "usage: $0 <task_name>"
    echo "All tasks: ${tasks[@]}"
fi


case $1 in
    "${tasks[0]}")     check;;
    "${tasks[1]}")     clean;;
    "${tasks[2]}")  cleanall;;
    "${tasks[3]}")     debug;;
    "${tasks[4]}")    docker;;
    "${tasks[5]}")       run;;
    "${tasks[6]}")      test;;
    "${tasks[7]}")    update;;
    "${tasks[8]}")      venv;;
esac
