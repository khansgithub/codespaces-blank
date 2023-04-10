#!/bin/bash

PORT=3333
docker run \
	-d \
	--name git \
	-v "$(pwd)/"entrypoint.sh:/usr/home/entrypoint.sh \
    -v "$(pwd)/"repo:/srv/repo \
	--entrypoint "/usr/home/entrypoint.sh" \
	--rm \
	-p $PORT:22 \
     --health-cmd "set -e;  nc -zv localhost 22; if [ $? -eq 0 ]; then exit 0; else exit 1; fi" \
     --health-interval=10s \
	alpine

# cd repo
# git init
# touch foo
# git add foo
# git config --local user.name "foo"
# git config --local user.email "foo@bar.com"
# git commit -m "initial commit"
# cd ~
# mkdir clone_dir

if [ ! -L /clone_dir ]; then
	sudo ln -s /home/codespace/codespaces-blank/mod /clone_dir
fi

# Wait for the container to become healthy
while true; do
    HEALTH=$(docker inspect --format='{{.State.Health.Status}}' git)
    if [ "$HEALTH" == "healthy" ]; then
        ssh-keyscan -p $PORT localhost >> ~/.ssh/known_hosts
        break
    else
        true
    fi
    sleep 5
done