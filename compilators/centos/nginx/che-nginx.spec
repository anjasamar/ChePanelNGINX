Name:           che-nginx
Version:        1.25.5
Release:        1%{?dist}
Summary:       Che Nginx - Web server for ChePanel

License:       GPL
URL:    https://chepanel.aldinara.co.id
Source0: https://nginx.org/download/nginx-1.25.5.tar.gz
Source1: logrotate
Source2: nginx.conf
Source3: nginx.default.conf
Source4: nginx.service
Source5: nginx.upgrade.sh
Source6: nginx.suse.logrotate
Source7: nginx-debug.service
Source8: nginx.copyright
Source9: nginx.check-reload.sh

%description
Che Nginx is a web server for ChePanel.

%prep
# we have no source, so nothing here

%build
tar -xzf $RPM_SOURCE_DIR/nginx-1.25.5.tar.gz -C $RPM_BUILD_DIR
cd nginx-1.25.5
./configure --prefix=/usr/local/che/nginx

%make_install
mv $RPM_BUILD_ROOT/usr/local/che/nginx/sbin/nginx $RPM_BUILD_ROOT/usr/local/che/nginx/sbin/che-nginx
rm -rf $RPM_BUILD_ROOT/usr/local/che/nginx/sbin/nginx.old
wget https://raw.githubusercontent.com/CheApps/ChePanelNGINX/main/compilators/debian/nginx/nginx.conf -O $RPM_BUILD_ROOT/usr/local/che/nginx/conf/nginx.conf

%files
/usr/local/che/nginx

%changelog
* Tue May 03 2024 Che Nginx Packaging <che-nginx-packaging@chepanel.com> - 1.25.5-1%{?dist}.ngx
- 1.25.5-1
- Initial release of Che Nginx 1.25.5
