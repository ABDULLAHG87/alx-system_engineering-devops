#!/usr/bin/env bash
# using puppet to make connection without password

# Define a class for configuring SSH client
class ssh_client_config {

# Install the 'openssh-client' package (if not already installed)
package { 'openssh-client':
  ensure => installed,
}

# Create the SSH configuration file
file { '/etc/ssh/ssh_config':
  ensure => present,
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
  notify => Service['ssh'],
}

# Declare identity file
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
  notify => Service['ssh'],
}

# Ensure the SSH service is running
service { 'ssh':
  ensure => running,
  enable => true,
}
