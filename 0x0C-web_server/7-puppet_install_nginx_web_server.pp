#installing of nginx with puppet

#installation of nginx package
package { 'nginx':
  ensure => installed,
}

#ensure running of nginx webserver
service { 'nginx':
  ensure => running,
  enable => true,
}

#creating a file for listening to port 80 of the webserver
# the file should contain return for redirection and 404 page error
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

# execute command for nginx restart
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
