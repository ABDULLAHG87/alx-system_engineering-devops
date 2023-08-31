#installing of nginx with puppet


package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

file { '/etc/nginx/sites-available/default':
  content => "
server {
    listen      80 default_server;
    listen      [::]:80 default_server;
    root        /etc/nginx/html;
    index       index.html index.htm;

    location / {
        return 200 'Hello World!';
    }

    location /redirect_me {
        return 301 'https://www.example.com';
    }
}
",
  require => Package['nginx'],
}

exec { 'nginx_reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  require     => File['/etc/nginx/sites-available/default'],
}

exec { 'nginx_test_config':
  command => '/usr/sbin/nginx -t',
  require => Exec['nginx_reload'],
}

Service['nginx'] ~> Exec['nginx_reload']
