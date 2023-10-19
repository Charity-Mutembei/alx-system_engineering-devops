# Define the user whose file limit needs to be adjusted
$target_user = 'holberton'

file { '/etc/security/limits.conf':
  ensure  => file,
  content => '#File erased',
}
