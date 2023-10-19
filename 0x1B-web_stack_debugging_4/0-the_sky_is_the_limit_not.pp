# Changes file limit details

exec { 'Increase nginx limit':
  command   => "sed -i 's/15/10000/' /etc/default/nginx",
  path      => '/usr/bin:/usr/local/bin:/bin',
  subscribe => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
}
