# Executes a command
exec{'pkill killmenow':
  command => '/usr/bin/pkill killmenow',
  returns => ['0', '1', '2', '3']
}
