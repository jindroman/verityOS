#!/usr/bin/env bash
# Build the Verity OS live/installer ISO.
# Run as root on Arch Linux (or in an archlinux container) with the `archiso` package installed:
#     sudo pacman -S archiso
#     sudo ./build.sh
# Result: ./out/verityos-<version>-x86_64.iso
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

VERSION="0.3.0-dev"
RELENG="${RELENG:-/usr/share/archiso/configs/releng}"
WORK=./work
OUT=./out
PROFILE=./profile

[[ $EUID -eq 0 ]] || { echo "Run as root: sudo ./build.sh" >&2; exit 1; }
command -v mkarchiso >/dev/null || { echo "mkarchiso not found — install it: pacman -S archiso" >&2; exit 1; }
[[ -d $RELENG ]] || { echo "archiso releng profile not found at $RELENG" >&2; exit 1; }

echo "==> Preparing profile from Arch releng…"
rm -rf "$PROFILE" "$WORK"
cp -r "$RELENG" "$PROFILE"

echo "==> Applying Verity identity…"
sed -i \
  -e 's|^iso_name=.*|iso_name="verityos"|' \
  -e 's|^iso_label=.*|iso_label="VERITYOS_$(date +%Y%m)"|' \
  -e 's|^iso_publisher=.*|iso_publisher="Verity OS"|' \
  -e 's|^iso_application=.*|iso_application="Verity OS Live/Installer"|' \
  -e "s|^iso_version=.*|iso_version=\"$VERSION\"|" \
  "$PROFILE/profiledef.sh"

# boot menu text (BIOS syslinux, GRUB, systemd-boot entries)
for d in syslinux grub efiboot; do
  [[ -d "$PROFILE/$d" ]] || continue
  grep -rlI "Arch Linux" "$PROFILE/$d" | xargs -r sed -i 's/Arch Linux/Verity OS/g' || true
done

echo "==> Adding packages…"
grep -vE '^\s*(#|$)' overlay/packages.verity >> "$PROFILE/packages.x86_64"
sort -u -o "$PROFILE/packages.x86_64" "$PROFILE/packages.x86_64"

echo "==> Overlaying Verity files…"
cp -a overlay/airootfs/. "$PROFILE/airootfs/"
cat >> "$PROFILE/profiledef.sh" <<'PERMS'

file_permissions+=(
  ["/usr/local/bin/verity"]="0:0:755"
  ["/usr/local/bin/verityfetch"]="0:0:755"
  ["/usr/local/bin/verity-install"]="0:0:755"
)
PERMS

echo "==> Building ISO (needs network; takes a few minutes)…"
mkdir -p "$OUT"
mkarchiso -v -w "$WORK" -o "$OUT" "$PROFILE"

echo
echo "Done:"
ls -lh "$OUT"/*.iso
(cd "$OUT" && sha256sum ./*.iso | tee SHA256SUMS)
