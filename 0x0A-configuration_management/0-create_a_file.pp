#TASK 0 = CREATE A FILE
#This code creates a puppet file in /tmp folder

file { '/tmp/school':
  ensure  => 'file',
  module  => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}