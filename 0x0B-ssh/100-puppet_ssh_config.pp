# set up your client SSH configuration file
include stdlib
file_line { 'Identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
}

file_line { 'No Passwdord needed':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}
