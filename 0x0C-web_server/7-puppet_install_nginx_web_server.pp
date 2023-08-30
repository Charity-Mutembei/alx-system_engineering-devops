class nginx_configuration {
  exec { 'add nginx stable repo':
    command => 'sudo add-apt-repository ppa:nginx/stable',
    path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  }

  exec { 'update packages':
    command => 'apt-get update',
    path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
    require => Exec['add nginx stable repo'],
  }

  package { 'nginx':
    ensure => installed,
    require => Exec['update packages'],
  }

  exec { 'allow HTTP':
    command => "ufw allow 'Nginx HTTP'",
    path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
    onlyif  => '! dpkg -l nginx | egrep \'îi.*nginx\' > /dev/null 2>&1',
    require => Package['nginx'],
  }

  exec { 'chmod www folder':
    command => 'chmod -R 755 /var/www',
    path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    content => "Hello World!\n",
    require => Package['nginx'],
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page\n",
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    path    => '/etc/nginx/sites-enabled/default',
    content => template('nginx_configuration/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  exec { 'restart nginx':
    command => 'service nginx restart',
    path    => ['/usr/bin', '/usr/sbin', '/bin'],
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
  }
}

file { '/etc/puppetlabs/code/environments/production/manifests/nginx_config.pp':
  ensure => present,
  content => inline_template('<%= scope.function_template("nginx_configuration/nginx_config.erb") %>'),
}