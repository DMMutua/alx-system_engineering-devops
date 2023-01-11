# Manifest for Installing `flask` version 2.1.0 using `pip3` package manager
package { 'flask':
  ensure => '2.1.0',
  provider => 'pip3',
}
