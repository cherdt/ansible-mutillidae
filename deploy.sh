#!/bin/bash

echo "Enter the target host or hosts (separated by commas). Note that you must have sudo privileges on each target host:"

read TARGET_HOSTS

ansible-playbook --become \
	         --ask-pass \
		 --ask-become-pass \
                 --inventory $TARGET_HOSTS, \
	         site.yml

