# Cockpit ZFS Manager

[![GitHub Tag](https://img.shields.io/github/v/release/nv6/cockpit-zfs-manager?include_prereleases&style=flat-square&color=brightgreen)](https://github.com/nv6/cockpit-zfs-manager/releases)

**An interactive ZFS on Linux admin package for Cockpit (with UI font fixes)**

## Requirements

* Cockpit: 201+
* NFS (Optional)
* Samba: 4+ (Optional)
* ZFS: 0.8+

### Tested Distributions

* Ubuntu 20.04 LTS
* AlmaLinux 9

## Installation

```bash
git clone https://github.com/nv6/cockpit-zfs-manager.git
cd cockpit-zfs-manager
tar -C src -xf fontpack.tar.gz
sudo cp -R src/* /usr/share/cockpit
```

> [!note]
> `fontpack.tar.gz` contains the missing UI fonts mentioned in https://github.com/45Drives/cockpit-zfs-manager/issues/34#issuecomment-2907588768

#### Samba

_see [original README](https://github.com/45Drives/cockpit-zfs-manager/blob/fc98e5a3c74ec5ed03b246c54e301e2c4661566b/README.md#samba)_

## Using Cockpit ZFS Manager

Login to Cockpit as a privileged user and click ZFS from the navigation list.

A Welcome to Cockpit ZFS Manager modal will display and allow you to configure initial settings.

Note: Inline help is currently available in modals. Documentation will be created at a later date.

## Notes

### Storage Pools

New storage pools are created with the following properties set (not visible in Create Storage Pool modal):
```
aclinherit=passthrough
acltype=posixacl
casesensitivity=sensitive
normalization=formD
sharenfs=off
sharesmb=off
utf8only=on
xattr=sa
```
### File Systems

New file systems are created with the following properties set (not visible in Create File System modal):
```
normalization=formD
utf8only=on
```
Passphrase is currently supported for encrypted file systems.

If SELinux contexts for Samba is selected, the following properties are set:
```
context=system_u:object_r:samba_share_t:s0
fscontext=system_u:object_r:samba_share_t:s0
defcontext=system_u:object_r:samba_share_t:s0
rootcontext=system_u:object_r:samba_share_t:s0
```

### Samba

ZFS always creates shares in /var/lib/samba/usershares folder when ShareSMB property is enabled. This is also the case even if Cockpit ZFS Manager is managing the shares. To avoid duplicate shares of the same file system, it is recommended to configure a different usershares folder path if required or to disable usershares in the Samba configuration file.

If enabled, Cockpit ZFS Manager manages shares for the file systems only. Samba global configuration will need to be configured externally.
