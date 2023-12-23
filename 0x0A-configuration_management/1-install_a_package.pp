# install a package with puppet

# Ensure 'pip3' is installed
package { 'python3-pip:
  ensure  => present,
}

# Install flask version 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}