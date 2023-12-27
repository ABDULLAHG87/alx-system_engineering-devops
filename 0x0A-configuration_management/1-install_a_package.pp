# install a package with pupet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
