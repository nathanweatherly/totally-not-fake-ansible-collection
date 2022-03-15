load: 
	./scripts/load.sh

run:
	# cp ./playbooks/tasks/hello-world.yml .
	ansible-playbook ./playbooks/tasks/hello-world.yml
	# rm ./hello-world.yml