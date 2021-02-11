# Ubuntu 20.04 as an Active Directory Domain Services (AD DS) Member

## WIP

> Assumption is made that this is a newly installed base system
>
> Replace *DOMAIN* with AD DS NetBIOS Name and *domain.example.com* with AD DS FQDN

### Cockpit

Install Cockpit and ZFS manager from 45Drives Repo

```sh
$ wget -qO - http://images.45drives.com/repo/keys/aptpubkey.asc | apt-key add -
$ curl -o /etc/apt/sources.list.d/45drives.list http://images.45drives.com/repo/debian/45drives.list
$ apt update
$ apt install cockpit cockpit-zfs-manager 
```

Firewall

```bash
$ sudo firewall-cmd --permanent --zone=public --add-service=cockpit
$ sudo firewall-cmd --reload
```

### ZFS

Install ZFS DKMS

```bash
apt install zfs-dkms
```

### Realmd

Install realmd from 45dives apt repo
```bash
apt install realmd
```
Edit realmd to use winbind instead of sssd by default
```bash
vim /usr/lib/realmd/realmd-defaults.conf
```
Under "[active-directory]" change sssd to winbind
default-client = winbind

Restart realmd
```bash
systemctl restart realmd
```

### Samba

Install Samba

```bash
apt install samba winbind
```

Remove default smb.conf
```bash
rm /etc/samba/smb.conf
```
Join Domain in Cockpit UI
Overview -> Configuration -> Join Domain
Required feilds are
  * Domain Address (ex. 45lab.local)
  * Domain Administrator Name (ex. A Domain user with rights to join machines to domain)
  * Domain Administrator Password

Alternatively, use the command line:
```bash
realm join DOMAIN.NAME -U user 
```

Start Samba

```bash
$ sudo systemctl start smb
```

Verify information is retrieved from AD DS:

```
$ sudo getent passwd "DOMAIN\Administrator"
$ sudo getent group "DOMAIN\Domain Users"
$ sudo wbinfo -g
$ sudo wbinfo -u
```

Edit Samba configuration file and set the AD DS schema mode, ACLs and Previous Versions properties:

```bash
$ sudo nano /etc/samba/smb.conf
```

Append to [global] section

```
idmap config DOMAIN : schema_mode = rfc2307

vfs objects = acl_xattr shadow_copy2
store dos attributes = yes
map acl inherit = yes
inherit acls = yes
inherit permissions = yes
				
shadow: snapdir = .zfs/snapshot
shadow: sort = desc
shadow: format = %Y.%m.%d-%H.%M.%S
shadow: localtime = yes

admin users = @"DOMAIN\Domain Admins"
```

Reload Samba configuration:

```bash
$ sudo smbcontrol all reload-config
```

Grant Disk Operator Privileges:

```bash
$ sudo net rpc rights grant "DOMAIN\Domain Admins" SeDiskOperatorPrivilege -U "DOMAIN\Administrator"
$ sudo net rpc rights grant "DOMAIN\Enterprise Admins" SeDiskOperatorPrivilege -U "DOMAIN\Administrator"
```

Create firewall rules for Samba:

```bash
$ sudo firewall-cmd --permanent --add-service=samba
$ sudo firewall-cmd --reload
```

Restart and Enable Samba service:

```bash
$ sudo systemctl restart smb
$ sudo systemctl enable smb
```

