#!/bin/bash
# Vault Wrap-Up Helper — collects git state for this vault.
#
# Single repo (this vault). No separate content repo. Add more entries
# to REPOS if/when sub-vaults or downstream repos appear.

VAULT_ROOT="/Users/charuwatnaranong/Desktop/Fin/trade-for-a-living"
REPOS=(
  "vault:${VAULT_ROOT}"
)
DATE=$(date +%Y-%m-%d)

echo "=== Git State ($DATE) ==="
for entry in "${REPOS[@]}"; do
  name="${entry%%:*}"
  path="${entry#*:}"
  [ -d "$path" ] || continue
  echo "### $name"
  echo "Branch: $(git -C "$path" branch --show-current 2>/dev/null)"
  echo "Latest: $(git -C "$path" log --oneline -1 2>/dev/null)"
  echo "Changes: $(git -C "$path" status --short 2>/dev/null || echo 'clean')"
  echo ""
done

echo "=== Log Entry Template ==="
echo "## [$DATE] session-end | <one-line summary>"

echo ""
echo "=== Remote ==="
git -C "$VAULT_ROOT" remote -v 2>/dev/null
