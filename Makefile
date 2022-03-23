run-hello-role:
	cp ./playbooks/tasks/hello-world-role.yml .
	ansible-playbook ./playbooks/tasks/hello-world-role.yml
	rm ./hello-world-role.yml

run-hello-mod:
	cp ./playbooks/tasks/hello-world-mod.yml .
	ansible-playbook ./playbooks/tasks/hello-world-mod.yml
	rm ./hello-world-mod.yml

run-goodbye-mod:
	cp ./playbooks/tasks/goodbye-world-mod.yml .
	ansible-playbook ./playbooks/tasks/goodbye-world-mod.yml
	rm ./goodbye-world-mod.yml

get-version:
	@cat ./galaxy.yml | grep 'version: ' | cut -d ' ' -f 2