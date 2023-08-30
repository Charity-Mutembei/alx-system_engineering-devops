# Install and configure Nginx
class nginx_config {
  package { 'nginx':
    ensure => present,
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
    require => Package['nginx'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => link,
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
  }

  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page",
    require => Package['nginx'],
  }
}

class nginx_redirect {
  file { '/etc/nginx/sites-available/redirect.conf':
    ensure  => present,
    content => template('nginx/redirect.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/redirect.conf':
    ensure  => link,
    target  => '/etc/nginx/sites-available/redirect.conf',
    require => File['/etc/nginx/sites-available/redirect.conf'],
    notify  => Service['nginx'],
  }
}

include nginx_config
include nginx_redirect