# Define the user whose file limit needs to be adjusted
$target_user = 'holberton'

include stdlib

file_line { 'remove_contents':
  ensure => absent,
  line   => '#File erased',
  match  => '^.*',
  path   => '/etc/security/limits.conf',
}

