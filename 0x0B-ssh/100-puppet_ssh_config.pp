#change SSH configuration file using puppet

file { '~/.ssh/config':
  ensure  => present,
  content => "
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  mode    => '0600',
  owner   => 'root',
  group   => 'root',
}
