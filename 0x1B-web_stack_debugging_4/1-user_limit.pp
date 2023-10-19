# Define the user whose file limit needs to be adjusted
$target_user = 'holberton'

file { 'loginFile':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#File erased'
}