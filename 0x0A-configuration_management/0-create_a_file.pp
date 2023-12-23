# TASK 0 = CREATE A FILE
# This code creates a puppet file in /tmp folder

file { 'school':
  ensure  => 'present',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  path    => '/tmp/school',
}