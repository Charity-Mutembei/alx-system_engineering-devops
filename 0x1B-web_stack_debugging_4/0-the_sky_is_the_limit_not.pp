# Changes file limit details

exec {
  command   => "sed -i 's/15/20000/' /etc/default/nginx",
  path      => '/usr/bin:/usr/local/bin:/bin',
  subscribe => Service['nginx'],
}

service { 'nginx':
  ensure => 'running',
}
