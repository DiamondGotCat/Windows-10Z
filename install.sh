#!/bin/bash

mkdir /etc/windows/
cp ./etc/windows/* /etc/windows/
cp ./usr/local/bin/* /usr/local/bin/

# テーマをインストール
cp -r "/etc/windows/Windows-10-Theme"/* "/usr/share/themes/"
cp -r "/etc/windows/Windows-10-Theme/extra-icons" "/usr/share/icons/Win10Z"

# 壁紙
mkdir -p "/usr/share/backgrounds/"
cp "/etc/windows/Windows-10-Theme/wallpaper.jpg" "/usr/share/backgrounds/win10z.jpg"

# XFCEパネル設定を/etc/skelに展開
mkdir -p "/etc/skel/.config/xfce4/"
tar -xvjf "/etc/windows/panel-config.tar.bz2" -C "/etc/skel/.config/xfce4/"

# plymouthテーマをコピー
mkdir -p "/usr/share/plymouth/themes/win10"
cp -r "/etc/windows/Windows-10-Start/"* "/usr/share/plymouth/themes/win10/"

# plymouthテーマの設定
echo 'GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"' >> "/etc/default/grub"
echo 'GRUB_GFXPAYLOAD_LINUX=keep' >> "/etc/default/grub"
sed -i 's/^PLYMOUTH_THEME=.*/PLYMOUTH_THEME="win10"/' "/etc/plymouth/plymouthd.conf"

# XFCEのテーマを新ユーザーに適用（~/.xprofile 経由）
cat >> "/etc/skel/.xprofile" <<EOF
xfconf-query -c xsettings -p /Net/ThemeName -s "Windows-10-Theme"
xfconf-query -c xsettings -p /Net/IconThemeName -s "Win10Z"
xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s "/usr/share/backgrounds/win10z.jpg"
EOF

echo "Setting Completed. Please Reboot to Apply Theme. Thanks for using!"

exit 0
