# Category Checklist - Desktop / Mobile Utility

Use when the target is an installed app: desktop utilities, mobile apps, CLI tools with a GUI, Electron apps. Work these axes while drafting docs 02, 04, 07, 08.

## Platform and distribution

- OS support matrix (Windows/macOS/Linux, versions) as *claimed* on the site
- Distribution channels: website download, Microsoft Store, Homebrew, App Store, Flathub
- Architecture: native, Electron, Qt, web-wrapper - infer from site/repo; label INFERRED
- Auto-update mechanism if mentioned

## System surface (what the app touches)

- File system access scope (whole-disk, user-selected folders, sandbox)
- Network usage (telemetry, cloud sync, license checks) - usually underdocumented → open question
- Privileges: admin/root required? drivers? kernel extensions?
- Integrations: shell context menus, global hotkeys, browser extensions

## Offline vs online behavior

- Does core function work offline? (Critical for utilities; rarely stated clearly → verify or UNKNOWN)
- Account requirement for basic features
- Sync/backup if present

## Licensing model

- Free / freemium / one-time / subscription - from pricing page
- License key mechanics if documented
- Open-source components (from repo NOTICE/THIRD-PARTY if public)

## Performance claims

- File size / duration / resolution limits
- Speed or benchmark claims → NOT TESTED unless from a neutral third party
- Resource requirements (RAM, GPU)

## Install / uninstall

- Installer vs portable vs store-managed
- Leftover data on uninstall (rarely documented → open question)
- Silent-install / enterprise deployment docs if present

## Test-plan seeds (docs/10)

- Offline: core conversion/edit works with network disabled (where VERIFIED offline)
- Permissions: denied file access → expected error dialog/behavior
- Platform parity: feature claimed on Windows only does not silently fail on macOS
- Uninstall leaves user data per documented policy (or UNKNOWN)

## Clean-room note

Desktop specs often under-document system behavior because the public site says little. That is fine: record UNKNOWNs in 13 rather than inventing sandbox/telemetry details. The rebuild can be *more* transparent than the original.
