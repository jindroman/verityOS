# verityos

  # 🟡 Verity OS

> **A Linux operating system with a personality.**

Verity OS is an experimental Linux distribution concept built around a simple idea:

**Your operating system shouldn't just work. It should talk to you.**

Verity combines a Linux desktop environment with a custom command-line experience, an AI-powered assistant, a 3D Verity orb, and its own package-management interface.

![Verity OS](https://placehold.co/1200x500/090909/FFD21A?text=VERITY+OS)

---

## ✨ Features

### 🔮 Verity AI

Meet **Verity** — a 3D orb that lives inside your desktop.

Verity is designed to:

* Talk to you using an AI voice
* Help with terminal commands
* Explain system errors
* Diagnose problems
* Manage packages
* Control parts of your desktop
* Eventually become your personal Linux assistant

Instead of:

```text
$ sudo apt install firefox
```

Verity aims for:

```text
$ sudo verity install firefox
```

And eventually:

```text
$ verity ask "install a browser and make it my default"
```

---

## 🖥️ Two Desktop Experiences

Verity OS is planned to ship with two pre-built desktop profiles.

### ⚡ Verity Hypr

A minimal, fast, keyboard-driven experience based around **Hyprland**.

Designed for:

* Power users
* Developers
* Keyboard workflows
* Performance
* Customization

### 🖥️ Verity Desktop

A more traditional graphical experience based around **KDE Plasma**.

Designed for:

* New Linux users
* Gaming
* Everyday computing
* Users who prefer a familiar desktop

You choose your experience during installation.

---

## 📦 The Verity Package Manager

Verity OS will eventually have its own frontend for Linux package management.

```bash
sudo verity install firefox
sudo verity remove firefox
sudo verity update
verity search discord
```

More advanced commands:

```bash
verity doctor
verity rollback
verity history
verity clean
verity sing                # plays the official Verity OS anthem 🎵
```

The goal isn't to replace the underlying Linux package ecosystem.

Instead, **Verity provides a simpler interface on top of it.**

---

## 🩺 Verity Doctor

Something broken?

Try:

```bash
verity doctor
```

Verity will inspect things such as:

```text
✓ Kernel
✓ Network
✓ Audio
✓ GPU
✓ Desktop
✓ Package database
✓ System services
⚠ 3 problems detected
```

Eventually, Verity should be able to explain what went wrong and offer to fix it.

---

## 💾 Safe Updates & Rollbacks

Verity OS is planned around a snapshot-based system.

> **Status:** `verity update` / `verity install` already try to snapshot first, but the current installer doesn't set up btrfs + snapper yet — the snapshot step is skipped with a warning.

Before major updates:

```text
Creating snapshot...
✓ Snapshot created

Updating system...
✓ Packages updated

Verity OS has been updated successfully.
```

If something goes wrong:

```bash
verity rollback
```

The goal is to make experimenting with Linux much less scary.

---

## 🎨 Verityfetch

Verity OS comes with its own system-information tool:

```bash
verityfetch
```

Example:

```text
                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                           ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                        ▒▒▒▒▒░██████████████▓███▒▒▒▒▒▒▒
                     ▒▒▒▒░████████████████████████▓█░▒▒▒▒
                   ▒▒▒▒████████████████████████████████▒▒▒▒▒
                 ▒▒▒▒       ██   █████   █   ░   █      █▒▒▒▒
               ░▒▒▒███  ██████  ██████  ████  ██ █  ███▓██▓▒▒▒▒
              ▒▒▒▓████ ▓   ███  ██████  ████░ ▒███ ▒   ██████▒▒▒
             ▒▒▒██████  ███ ██      ██  ▒███   ███ ▓ ██ ██████▒▒▒
            ▒▒▒███████████████████████████████████████████▓██▓█▒▒▒
           ▒▒▒██████  █  █ ██▒██▓ ██    █ █   █ █  █ █▒▓██░██▓█▓▒▒▒
           ▒▒ ██████   █ ▓     █   █░█▓█░██ █ █    █  █  █  █████▒▒
          ▒▒▒████████████████████░           ████████████████▓██▓▒▒▒
          ▒▒░█████████▓▓▓▓█████                ███████▓███████████▒▒
          ▒▒██████▓▓▒▓██▓█▓▓▓▓▒                 ███▒▓▓█████▓▓█▓███▒▒▒
         ░▒▒█████▓▓▓█▓▓▓▒▒▒▓█▓▒    █████   ███   █████████████▓███▒▒▒
          ▒▒███████▓░▓█▓▓▓▒▓ ▓▓                   █▓▓▓█▒▓▓▒███▓▓▓▓▒▒▒
          ▒▒███▓▓▓██▓▓▓▓▒▒▓█░▓▓▓░  ███████████    █▓▓▒▓██████████▓▒▒▒
          ▒▒ ██▓███  ███▓▓▓█▒▒▒▓▓░  ░██  ▓░█▓█    █▓▓▓▓▓▒ ███▓▓▓██▒▒
          ▒▒▒████ ▓▓█▒ ██▓█ █░▒▓▓▓▒ ░▓██▓█  █      ▓▓▓▒░██▓ ███▓█▒▒▒
           ▒▒░█  ███▒█▒ ███░▒█▒▒▒▓█▓           ░░ ███░▒█▒█▓▓  █▓█▒▒▒
           ▒▒▒███▒█▓▒██ ░  █░  █▓░▒▓█████▓▒░  ░ ░    ██▓▒▓ ▓▓██▓▒▒▒
            ▒▒▒█▓▓▒▒▓▓▒███ ▓███████ ░▓     ████░▒█ ██  █▓▓▓░███▒▒▒
             ▒▒▒██▓▒░▓▒▓█  ░██ █████ █░█ ▓ ███▒██▓  ██  ░  ██▓▒▒▒
              ▒▒▒███████░  ██▒███ ██░▒  ░  ███ █ ████████████▒▒▒
               ░▒▒▒▓▓██████▓████░▓██████████▓█████░▒████▓▓▓░▒▒▒
                 ▒▒▒▒███████▓█▓▓██▓▓██▓██▓▓█▓█▓▓▓███████▓█▒▒▒▒
                  ▒▒▒▒░▓▒▒ █████▓▓▓▓▓▓▒█▒▒▓█▓▒ ▓▓▒ ▒█▓▓▓▒▒▒▒
                     ▒▒▒▒▓▒▓▓█▓▓▓█▓██▓▓▓░▒▒▓▒▓▒▒▒▒░▒█▒▒▒▒░
                       ▒▒▒▒▒▒█▓▒▓▓▒▓▒▒▓▓▒▓▒▒▒▒▒░▒▒▒▒▒▒▒
                           ▒▒▒▒▒▒▒▒▒▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
                                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒

verity@system
──────────────────────────────
OS          Verity OS
Kernel      Linux
Desktop     Hyprland
Shell       zsh
Assistant   Verity AI
```

---

## 🧠 Project Philosophy

Verity OS isn't trying to make Linux complicated.

It's trying to make Linux **feel alive**.

The design philosophy is:

> **Powerful underneath. Simple on top.**

Advanced users should still have access to the normal Linux ecosystem, terminals, configuration files and tools.

New users should have Verity there to explain what everything means.

---

## 🛠️ Planned Architecture

```text
                    ┌─────────────────┐
                    │    Verity AI    │
                    │   Voice + LLM   │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   Verity Orb    │
                    │   3D Assistant  │
                    └────────┬────────┘
                             │
              ┌──────────────▼──────────────┐
              │        Verity CLI           │
              │  install / doctor / update  │
              │  rollback / search / ask    │
              └──────────────┬──────────────┘
                             │
                 ┌───────────▼───────────┐
                 │    Linux / Arch       │
                 │   Package Ecosystem   │
                 └───────────┬───────────┘
                             │
                ┌────────────▼────────────┐
                │        Linux Kernel    │
                └─────────────────────────┘
```

---

## 🚧 Current Status

**Early development — v0.4.4. The ISO builds in CI, boots and installs in a VM (VirtualBox); not yet tested on real hardware.**

Currently being worked on:

* [x] Verity branding
* [x] Verity ASCII logo
* [x] Verity OS web prototype (early draft, no longer in the repo)
* [x] Initial CLI concept
* [x] Package manager concept
* [x] Desktop concepts
* [x] Real Arch-based ISO — archiso build profile (`build.sh`) + CI release workflow, booted in a VM
* [x] Real `verity` package manager — CLI wrapping pacman (`verity install/remove/update/search/history/clean/rollback`)
* [x] Hyprland profile — package list + starter config
* [x] KDE profile — package list
* [ ] 3D Verity orb
* [ ] AI voice
* [x] System diagnostics — basic `verity doctor`
* [ ] Snapshot/rollback system — not wired up yet (installer uses ext4; `verity rollback` needs btrfs + snapper)
* [x] Installer — terminal installer (`verity-install`), dry-run supported
* [ ] Verity repositories

---

## 🚀 Build, test & install

> ⚠️ **Experimental.** The installer erases a whole disk. Try it in a virtual machine first.

### 1. Build the ISO

**Option A — GitHub Actions (no Arch machine needed).**
Go to **Actions → Build Verity OS ISO → Run workflow**, or push a tag like `v0.4.3`.
The finished ISO is attached to the run (and to the Release, for tags).

**Option B — on Arch Linux (or an `archlinux` container):**

```bash
sudo pacman -S archiso
sudo ./build.sh
# → out/verityos-<version>-x86_64.iso  (+ SHA256SUMS)
```

The version comes from the `VERSION` file (CI overrides it with the git tag).

### 2. Try it in a VM

```bash
sudo pacman -S qemu-full          # or your distro's QEMU
./test-vm.sh                      # BIOS boot
./test-vm.sh --uefi               # UEFI boot (needs edk2-ovmf)
```

Tip: if you pick **Verity Hypr** inside a VM and the desktop won't start, the VM probably has no 3D acceleration — choose **Verity Desktop** or **Terminal only** to test, or try on real hardware / a GPU-passthrough VM.

### 3. Install

Boot the ISO, then run:

```bash
verity-install            # interactive installer
verity-install --dry-run  # walk the menus, change nothing, print the commands
```

The installer will:

1. Check boot mode (UEFI/BIOS) and internet (with a Wi-Fi fallback)
2. Let you pick a disk (the live USB is hidden; disks under 12 GB are refused) and make you type its name to confirm — the summary shows how much storage the chosen edition needs
3. Let you choose **Verity Hypr**, **Verity Desktop** (KDE) or **Terminal only**
4. Ask for keymap, hostname, time zone, username and password
5. Partition (GPT): 1 GiB FAT32 boot (UEFI) or bios_grub (BIOS), rest ext4 root
6. Install Arch base + your desktop with `pacstrap`, then Verity tools & branding
7. Install GRUB (UEFI: boot entry + fallback path so VirtualBox still boots)

A log is written to `/tmp/verity-install.log`.

### Troubleshooting

* **Login bounces straight back to the greeter — the password seems broken.** The Hyprland desktop needs 3D acceleration: in VirtualBox go to *Settings → Display → Enable 3D Acceleration* and restart the VM. (The installer warns about this too; **Verity Desktop** (KDE) works without 3D.)
* **After reboot the installer starts again.** The installer ejects the install medium before rebooting; if the machine still picks the ISO/USB, remove it when the screen goes black (in the VM: *Devices → Optical Drives → Remove disk from virtual drive*).
* **`verity sing` plays nothing.** Check `verity doctor` for audio and make sure the VM has an audio controller (*Settings → Audio*).

### Writing the ISO to a USB stick

```bash
sudo dd if=out/verityos-*.iso of=/dev/sdX bs=4M status=progress oflag=sync   # double-check sdX!
```

(or use Ventoy / balenaEtcher)

### Repository layout

```text
VERSION                  current version number (CI overrides it from the git tag)
build.sh                 builds the ISO from Arch's archiso "releng" profile + overlay/
test-vm.sh               boots the ISO in QEMU
overlay/
  packages.verity        extra packages for the live ISO
  airootfs/              files copied into the live system
    usr/local/bin/       verity, verity-ask, verityfetch, verity-install, verity-setup-desktop
    usr/share/verity/    logo, os-release, desktop profiles
    etc/pacman.d/hooks/  re-applies Verity branding after pacman updates
.github/workflows/       CI that builds the ISO
```

### Where should the ISO live?

Don't commit `.iso` files with Git LFS and expect "Download ZIP" to include them — GitHub's ZIP only contains the tiny LFS *pointer* file. Publish ISOs as **GitHub Releases** assets (the workflow above does this for tags).

### Known limitations (v0.4.4)

* Boots and installs in a VM; not yet tested on real hardware
* The installer creates a single **ext4** root partition — btrfs subvolumes, snapshots and `verity rollback` are **not set up yet** (rollback reports this and exits)
* `verity ask` works offline via its built-in knowledge base (and can use Ollama/Claude if you set it up); the 3D orb and AI voice are **not implemented yet**
* x86_64 only; no Secure Boot support; no disk encryption yet
* Hyprland profile is minimal; KDE profile is stock Plasma
* **Verity Hypr (Hyprland) needs 3D acceleration** — enable it in the VM (*Settings → Display → Enable 3D Acceleration*) or the desktop won't start and the login screen appears broken; Verity Desktop (KDE) works without it

---

## 🗺️ Roadmap

### Phase 1 — Identity

* Verity branding
* UI design
* Terminal experience
* `verityfetch`
* Website

### Phase 2 — Linux Base

* Arch Linux base
* Installer
* Hardware detection
* Networking
* Audio
* GPU support

### Phase 3 — Desktop

* Verity Hypr
* Verity Desktop
* Themes
* Wallpapers
* Panel
* Notifications

### Phase 4 — Verity

* 3D orb
* AI backend
* Voice synthesis
* Speech recognition
* Terminal integration

### Phase 5 — Ecosystem

* Verity repositories
* Package manager
* Extensions
* Themes
* Plugins
* Community packages

---

## 🤝 Contributing

Verity OS is an experimental project and contributions are welcome.

Ideas, UI concepts, Linux development, package management, AI integration, desktop development and terrible jokes are all welcome.

If you have an idea:

1. Fork the repository
2. Create a branch
3. Make your changes
4. Open a pull request

---

## ⚠️ Disclaimer

Verity OS is currently experimental.

Do **not** install early development builds on a machine containing important data.

The project is still evolving rapidly and commands, architecture and features may change.

---

## 🟡 Verity

**Linux, but it talks back.**

```text
$ verity ask "what can you do?"

> Pretty much anything.
> Give me a minute.
```

---

### License

License information will be added as the project matures.
