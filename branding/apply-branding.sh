#!/usr/bin/env bash
# apply-branding.sh <archiso-profile-dir>
# Swaps the Arch logo and names in the ISO boot menus for Verity OS.
# Call it from build.sh AFTER the archiso profile has been copied into place
# and BEFORE mkarchiso runs.
set -euo pipefail

P="${1:?usage: apply-branding.sh <archiso-profile-dir>}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# BIOS boot menu logo
if [[ -d "$P/syslinux" ]]; then
  cp "$HERE/splash.png" "$P/syslinux/splash.png"
fi

# Boot menu titles (BIOS syslinux, UEFI GRUB, UEFI systemd-boot)
for f in "$P"/syslinux/*.cfg "$P"/grub/*.cfg "$P"/efiboot/loader/entries/*.conf; do
  [[ -f "$f" ]] || continue
  sed -i 's/Arch Linux install medium/Verity OS/g; s/Arch Linux/Verity OS/g' "$f"
done

# ISO name / volume label
if [[ -f "$P/profiledef.sh" ]]; then
  sed -i \
    -e 's|^iso_name=.*|iso_name="verityos"|' \
    -e 's|^iso_label=.*|iso_label="VERITY_$(date +%Y%m)"|' \
    -e 's|^iso_application=.*|iso_application="Verity OS Live/Install"|' \
    "$P/profiledef.sh"
fi

echo "[branding] Verity OS branding applied to $P"
