all:

install:
	mkdir -p $(DESTDIR)/usr/share/cockpit
	cp -r src/* $(DESTDIR)/usr/share/cockpit

uninstall:
	rm -rf $(DESTDIR)/usr/share/cockpit/zfs
	rm -rf $(DESTDIR)/etc/cockpit/zfs
