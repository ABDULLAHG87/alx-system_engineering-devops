#!/usr/bin/env bash
# using puppet to make connection without password

# Create the SSH configuration file
file { '/etc/ssh/ssh_config':
  ensure => present,
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
  match  => '^#?PasswordAuthentication',
}

# Declare identity file
file_line { 'Declare identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?IdentityFile',
}

# Ensure the SSH service is running
service { 'ssh':
  ensure => running,
  enable => true,
}
