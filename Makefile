run-role:
	cp ./playbooks/tasks/hello-world-role.yml .
	ansible-playbook ./playbooks/tasks/hello-world-role.yml
	rm ./hello-world-role.yml

run-mod:
	cp ./playbooks/tasks/hello-world-mod.yml .
	ansible-playbook ./playbooks/tasks/hello-world-mod.yml
	rm ./hello-world-mod.yml

get-version:
	@cat ./galaxy.yml | grep 'version: ' | cut -d ' ' -f 2