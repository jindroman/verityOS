# Verity OS default zsh config
autoload -Uz compinit && compinit
HISTFILE=~/.zsh_history; HISTSIZE=5000; SAVEHIST=5000
setopt SHARE_HISTORY HIST_IGNORE_DUPS
PROMPT=$'%F{220}verity%f %F{244}%~%f %# '
alias ls='ls --color=auto'; alias ll='ls -lah'
alias update='sudo verity update'
[[ -o login ]] && command -v verityfetch >/dev/null && verityfetch
