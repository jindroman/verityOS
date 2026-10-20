#!/usr/bin/env bash
# Boot the ISO in QEMU with a blank virtual disk, so you can try verity-install safely.
#   ./test-vm.sh            # BIOS boot
#   ./test-vm.sh --uefi     # UEFI boot (needs the edk2-ovmf package)
# After installing, run again with --disk-only to boot the installed system.
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")"

ISO="$(ls -t out/verityos-*.iso 2>/dev/null | head -1 || true)"
DISK=verity-test.qcow2
[[ -f $DISK ]] || qemu-img create -f qcow2 "$DISK" 30G

ARGS=(-m 4G -smp 2 -drive "file=$DISK,format=qcow2,if=virtio" -vga virtio -nic user,model=virtio-net-pci)
[[ -w /dev/kvm ]] && ARGS+=(-enable-kvm -cpu host) || echo "(no KVM — it will be slow)"

for a in "$@"; do
  case $a in
    --uefi)
      CODE=""
      for c in /usr/share/edk2/x64/OVMF_CODE.4m.fd /usr/share/edk2/x64/OVMF_CODE.fd /usr/share/OVMF/OVMF_CODE.fd; do
        [[ -f $c ]] && { CODE=$c; break; }
      done
      [[ -n $CODE ]] || { echo "OVMF firmware not found (install edk2-ovmf)"; exit 1; }
      ARGS+=(-drive "if=pflash,format=raw,readonly=on,file=$CODE") ;;
    --disk-only) ISO="" ;;
  esac
done

[[ -n "$ISO" ]] && ARGS+=(-cdrom "$ISO" -boot d)
exec qemu-system-x86_64 "${ARGS[@]}"
