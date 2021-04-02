# This puppet manifest creates a file

file { '/tmp/holberton':
  ensure  => present,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => www-data,
  group   => www-data
}
