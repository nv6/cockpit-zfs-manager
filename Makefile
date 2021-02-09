all:

install:
	mkdir -p $(DESTDIR)/usr/share/cockpit/zfs
	cp -r zfs/* $(DESTDIR)/usr/share/cockpit/

uninstall:
	rm -rf $(DESTDIR)/usr/share/cockpit/zfs