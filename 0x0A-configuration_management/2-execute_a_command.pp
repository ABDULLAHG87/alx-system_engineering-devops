# Execute a command with Puppet

exec { 'pkill -f killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/',
}